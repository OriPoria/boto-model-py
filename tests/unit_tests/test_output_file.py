from boto_model_py.output_file import create_output_file
from boto_model_py.temporary_file import create_temporary_file


def test_create_output_file():
    file_path = create_temporary_file({"Name": "Alice"})
    output_file_spec = create_output_file(
        output_path="./",
        boto_response_syntax_file_name="temp_file_name",
        preprocessed_file_path=file_path,
    )
    assert output_file_spec.main_class_name == "TempFileNameResponse"
