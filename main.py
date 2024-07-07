import os
import json
import argparse
import subprocess
import ast
import astor

from enum_writer import enum_classes_to_replace
from preprocessing import preprocess_input

DIST_FOLDER = "dist"



LINE_OF_BOOLEAN_PREFIX = "BOOL_LINE_NUMBER"
LINE_OF_ENUM_PREFIX = "ENUM_LINE_NUMBER"
LINE_OF_DATETIME_PREFIX = "DATETIME_LINE_NUMBER"




def find_path(dict_, value, path=None):
    # TODO: change parameter name to input, not necessarily be a dict as termination
    # If value is found in a list, path is not accurate as warning prints says
    if path is None:
        path = []
    if isinstance(dict_, str):
        print("Warning: found path to value inside a list, potentially need to be more specific with path")
        return path if dict_ == value else None
    for k, v in dict_.items():
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

def find_all_path_to_value(dict_json_: dict, list_of_values_in_json: list[str]) -> dict:
    result = dict()
    for v in list_of_values_in_json:
        result[v] = find_path(dict_json_, v)
    return result


def change_ast_field_type(ast_object_, dict_of_values: dict, actual_type: str):
    for list_of_path in dict_of_values.values():
        next_class = main_class_name
        list_of_path.insert(0, main_class_name)
        len_of_path = len(list_of_path)
        for index in range(0, len_of_path-1):
            for node in ast.walk(ast_object_):
                if isinstance(node, ast.ClassDef) and node.name == next_class:
                    next_attribute = list_of_path[index + 1]
                    for class_body_item in node.body:
                        if isinstance(class_body_item, ast.AnnAssign) and class_body_item.target.id == next_attribute:
                            def get_root_type(class_body_item_):
                                if "slice" in class_body_item_.__dict__:
                                    return get_root_type(class_body_item_.slice)
                                else:
                                    assert isinstance(class_body_item_, ast.Name)
                                    return class_body_item_.id
                            next_class = get_root_type(class_body_item.annotation)
                            if next_class == "str":
                                class_body_item.annotation.slice.id = actual_type


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate pydantic base model from boto3 response format")

    # Add arguments
    parser.add_argument('file_path', type=str, help='The path of the file definition')
    parser.add_argument('--with_metadata', action='store_true', help='Add response metadata to object')

    args = parser.parse_args()

    file_path = args.file_path
    with open(file_path) as f:
        s_ = f.read()
    file_name = os.path.basename(file_path)
    dict_json, lkod, lkob, lkwe, enum_dict, map_from_line_of_enum_to_list_of_values = preprocess_input(s_)
    map_from_value_of_temp_bool_to_list_of_path = find_all_path_to_value(dict_json, lkob)
    map_from_value_of_temp_enum_to_list_of_path = find_all_path_to_value(dict_json, lkwe)
    map_from_value_of_temp_datetime_to_list_of_path = find_all_path_to_value(dict_json, lkod)

    temp_json_path = "temp.json"
    with open(temp_json_path, "w") as f:
        json.dump(dict_json, f, indent=2)
    enum_classes_ast, enum_class_names = enum_classes_to_replace(dict_json, map_from_value_of_temp_enum_to_list_of_path, map_from_line_of_enum_to_list_of_values)
    ###### End process of json

    module_path = os.path.join(DIST_FOLDER, f"{file_name}_response.py")
    # Example command
    main_class_name = f"{file_name.title().replace('_', '')}Response"
    command = f"datamodel-codegen --input {temp_json_path} --output {module_path} --force-optional --class-name {main_class_name}"
    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    os.remove(temp_json_path)

    ##### Ast processing
    with open(module_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    source_code = source_code.replace(" = None", "")
    source_code = source_code.replace("(BaseModel):", "(BaseResponse):")


    with open("base_response.py", 'r', encoding='utf-8') as file:
        base_response_code = file.read()
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

    change_ast_field_type(ast_object, map_from_value_of_temp_datetime_to_list_of_path, "datetime")
    change_ast_field_type(ast_object, map_from_value_of_temp_bool_to_list_of_path, "bool")
    for enums_name_to_path in enum_class_names:
        change_ast_field_type(ast_object, enums_name_to_path, list(enums_name_to_path.keys())[0])

    if args.with_metadata:
        for node in ast.walk(ast_object):
            if isinstance(node, ast.ClassDef) and node.name == main_class_name:

                node.body.append(ast.parse("ResponseMetadata: Optional[dict]").body[0])
                print(f"Main class name: {node.name}")

    modified_code = astor.to_source(ast_object)
    # Print the modified code
    with open(module_path, 'w') as f:
        f.write(modified_code)
