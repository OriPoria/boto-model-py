import os
import subprocess
from dataclasses import dataclass


@dataclass
class OutputFileSpec:
    code_file: str
    main_class_name: str
    module_path: str


def create_output_file(
    output_path: str, boto_response_syntax_file_name: str, preprocessed_file_path: str
) -> OutputFileSpec:

    module_path = os.path.join(
        output_path, f"{boto_response_syntax_file_name}_response.py"
    )
    # Example command
    main_class_name = (
        f"{boto_response_syntax_file_name.title().replace('_', '')}Response"
    )
    command = f"datamodel-codegen --input {preprocessed_file_path} --output {module_path} --force-optional --class-name {main_class_name}"
    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"running 'datamodel-codegen' command failed.\nError from command: {result.stderr}"
        )
    os.remove(preprocessed_file_path)

    with open(module_path, "r", encoding="utf-8") as file:
        code_module_file = file.read()
    return OutputFileSpec(
        code_file=code_module_file,
        main_class_name=main_class_name,
        module_path=module_path,
    )
