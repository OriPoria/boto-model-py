import os
import ast
import astor
from typing import Union
from functools import partial
from dataclasses import dataclass

from boto_model_py.enum_writer import enum_classes_to_replace
from boto_model_py.output_file import create_output_file, OutputFileSpec
from boto_model_py.preprocessor import (
    preprocess_input,
    PreprocessedData,
    PreprocessException,
)
from boto_model_py.consts_source_code import base_response_code
from boto_model_py.temporary_file import create_temporary_file
from boto_model_py.ast_processor.field_type import change_ast_field_type, merge_imports, ImportSorter


def find_path(json_part: [Union[str, dict, list]], value, path=None):
    if path is None:
        path = []
    if isinstance(json_part, str):
        return path if json_part == value else None
    for k, v in json_part.items():
        current_path = path + [k]
        if v == value:
            return current_path
        elif isinstance(v, dict):
            result = find_path(v, value, current_path)
            if result:
                return result
        elif isinstance(v, list):
            for item in v:
                result = find_path(item, value, current_path)
                if result:
                    return result
    return None


def find_all_path_to_value(dict_json: dict, list_of_values_in_json: list[str]) -> dict:
    result = dict()
    for v in list_of_values_in_json:
        result[v] = find_path(json_part=dict_json, value=v)
    return result


def read_boto_response_syntax_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


@dataclass
class RunTransformationStatus:
    file_path: str
    file_name: str
    status: str


def run_transformation(
    file_path: str, output_path: str, with_metadata: bool = False
) -> RunTransformationStatus:
    boto_response_syntax_file_name = os.path.basename(file_path)
    input_file_string = read_boto_response_syntax_file(file_path=file_path)
    try:
        preprocessed_data = preprocess_input(input_file_string)
    except Exception as exp:
        print("Error occurred during preprocess", str(exp))
        return RunTransformationStatus(
            file_path=file_path, file_name=boto_response_syntax_file_name, status="FAIL"
        )
    find_all_path_to_value_partial = partial(
        find_all_path_to_value, dict_json=preprocessed_data.preprocessed_json
    )
    map_from_value_of_temp_bool_to_list_of_path = find_all_path_to_value_partial(
        list_of_values_in_json=preprocessed_data.key_line_boolean
    )
    map_from_value_of_temp_enum_to_list_of_path = find_all_path_to_value_partial(
        list_of_values_in_json=preprocessed_data.key_line_enum
    )
    map_from_value_of_temp_datetime_to_list_of_path = find_all_path_to_value_partial(
        list_of_values_in_json=preprocessed_data.key_line_datetime
    )

    preprocessed_file_path = create_temporary_file(preprocessed_data.preprocessed_json)

    enum_classes_ast, enum_class_names = enum_classes_to_replace(
        preprocessed_data.preprocessed_json,
        map_from_value_of_temp_enum_to_list_of_path,
        preprocessed_data.enum_line_values_map,
    )
    ###### End process of json

    output_file_spec = create_output_file(
        output_path=output_path,
        boto_response_syntax_file_name=boto_response_syntax_file_name,
        preprocessed_file_path=preprocessed_file_path,
    )
    source_code = output_file_spec.code_file.replace(" = None", "")
    source_code = source_code.replace("(BaseModel):", "(BaseResponse):")

    base_response_code_ast = ast.parse(base_response_code).body
    ast_object = ast.parse(source_code)

    for b_r in base_response_code_ast:
        if isinstance(b_r, ast.ImportFrom):
            ast_object.body.insert(1, b_r)
        else:
            ast_object.body.insert(3, b_r)
    if map_from_value_of_temp_datetime_to_list_of_path:
        ast_object.body.insert(1, ast.parse("from datetime import datetime").body[0])
    if map_from_value_of_temp_enum_to_list_of_path:
        ast_object.body.insert(1, ast.parse("from enum import Enum").body[0])

    for e_c in enum_classes_ast:
        ast_object.body.insert(3, e_c)

    change_ast_field_type(
        ast_object,
        map_from_value_of_temp_datetime_to_list_of_path,
        "datetime",
        output_file_spec.main_class_name,
    )
    change_ast_field_type(
        ast_object,
        map_from_value_of_temp_bool_to_list_of_path,
        "bool",
        output_file_spec.main_class_name,
    )
    for enums_name_to_path in enum_class_names:
        change_ast_field_type(
            ast_object,
            enums_name_to_path,
            list(enums_name_to_path.keys())[0],
            output_file_spec.main_class_name,
        )

    if with_metadata:
        for node in ast.walk(ast_object):
            if (
                isinstance(node, ast.ClassDef)
                and node.name == output_file_spec.main_class_name
            ):

                node.body.append(ast.parse("ResponseMetadata: Optional[dict]").body[0])
                print(f"Main class name: {node.name}")

    sorter = ImportSorter()
    sorter.transform(ast_object)
    modified_code = astor.to_source(ast_object)
    # Print the modified code
    with open(output_file_spec.module_path, "w") as f:
        f.write(modified_code)
    return RunTransformationStatus(
        file_path=file_path, file_name=boto_response_syntax_file_name, status="OK"
    )
