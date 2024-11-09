import ast

from .field_type import change_ast_field_type
from .imports_handler import append_source_imports_based_on_field_types_required
from .consts_source_code import base_response_code, datetime_type, bool_type, response_metadata_attr

from boto_model_py.preprocessor import PreprocessedData
from boto_model_py.output_file import OutputFileSpec


def convert_ast_object(source_code: str,
                       preprocessed_data: PreprocessedData,
                       output_file_spec: OutputFileSpec,
                       enum_classes_ast: list[ast.ClassDef],
                       enum_class_names) -> ast.Module:
    base_response_code_ast = ast.parse(base_response_code).body
    ast_object = ast.parse(source_code)
    ast_object = append_source_imports_based_on_field_types_required(ast_object,
                                                                     base_response_code_ast,
                                                                     preprocessed_data.key_line_datetime,
                                                                     preprocessed_data.key_line_enum,
                                                                     enum_classes_ast)
    change_ast_field_type(
        ast_object,
        preprocessed_data.key_line_datetime,
        datetime_type,
        output_file_spec.main_class_name,
    )
    change_ast_field_type(
        ast_object,
        preprocessed_data.key_line_boolean,
        bool_type,
        output_file_spec.main_class_name,
    )
    for enums_name_to_path in enum_class_names:
        change_ast_field_type(
            ast_object,
            enums_name_to_path,
            list(enums_name_to_path.keys())[0],
            output_file_spec.main_class_name,
        )
    return ast_object


def append_response_metadata_class(ast_object: ast.Module, output_file_spec: OutputFileSpec) -> ast.Module:
    for node in ast.walk(ast_object):
        if (
            isinstance(node, ast.ClassDef)
            and node.name == output_file_spec.main_class_name
        ):
            node.body.append(ast.parse(response_metadata_attr).body[0])
    return ast_object
