import os
from enum import Enum
from typing import Optional
from dataclasses import dataclass

from boto_model_py.enum_writer import enum_classes_to_replace
from boto_model_py.output_file import create_output_file, OutputFileSpec
from boto_model_py.preprocessor import (
    preprocess_input,
    PreprocessedData,
    PreprocessException,
)
from boto_model_py.temporary_file import create_temporary_file

from boto_model_py.ast_processor import convert_ast_object, handle_object_imports, append_response_metadata_class

from boto_model_py.source_code_editor import edit_source_code


def read_boto_response_syntax_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


class RunTransformationStatus(Enum):
    OK = "OK"
    FAIL = "FAIL"


@dataclass
class RunTransformationSummary:
    file_path: str
    file_name: str
    status: RunTransformationStatus
    result_output_path: Optional[str] = None
    message: Optional[str] = None


def run_transformation(
    file_path: str, output_path: str, with_metadata: bool = False
) -> RunTransformationSummary:
    boto_response_syntax_file_name = os.path.basename(file_path)
    input_file_string = read_boto_response_syntax_file(file_path=file_path)
    try:
        preprocessed_data = preprocess_input(input_file_string)
    except Exception as exp:
        return RunTransformationSummary(
            file_path=file_path, file_name=boto_response_syntax_file_name, status=RunTransformationStatus.FAIL, message=str(exp)
        )
    enum_classes_ast, enum_class_names = enum_classes_to_replace(
        preprocessed_data.preprocessed_json,
        preprocessed_data.key_line_enum,
        preprocessed_data.enum_line_values_map,
    )

    preprocessed_file_path = create_temporary_file(preprocessed_data.preprocessed_json)

    output_file_spec = create_output_file(
        output_path=output_path,
        boto_response_syntax_file_name=boto_response_syntax_file_name,
        preprocessed_file_path=preprocessed_file_path,
    )
    source_code = edit_source_code(output_file_spec.code_file)
    
    ast_object = convert_ast_object(source_code,
                                    preprocessed_data,
                                    output_file_spec,
                                    enum_classes_ast,
                                    enum_class_names)

    if with_metadata:
        append_response_metadata_class(ast_object, output_file_spec)
    modified_code: str = handle_object_imports(ast_object)
    # Print the modified code
    with open(output_file_spec.module_path, "w") as f:
        f.write(modified_code)
    return RunTransformationSummary(
        file_path=file_path, file_name=boto_response_syntax_file_name, status=RunTransformationStatus.OK,
        result_output_path=output_file_spec.module_path
    )
