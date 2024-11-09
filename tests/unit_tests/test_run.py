import os
import json
from unittest.mock import patch

from boto_model_py.preprocessor import PreprocessedData
from boto_model_py.run import run_transformation, RunTransformationSummary


def test_run_transformation():
    files_path = os.path.join("tests", "unit_tests", "files")
    mock_preprocess_data_path = os.path.join(files_path, "mock_preprocess_data.json")
    input_path = os.path.join(files_path, "list_buckets")
    output_folder_path = os.path.join(files_path)
    expected_output_response_path = os.path.join(
        files_path, "expected_list_buckets_response.txt"
    )

    with open(mock_preprocess_data_path) as f:
        mock_preprocessed_data = PreprocessedData(**json.load(f))

    with patch(
        "boto_model_py.run.preprocess_input", return_value=mock_preprocessed_data
    ):
        result = run_transformation(input_path, output_folder_path, False)

    result_output_path = os.path.join(output_folder_path, "list_buckets_response.py")

    assert result.result_output_path == result_output_path

    with open(expected_output_response_path) as f1, open(result_output_path) as f2:
        assert f1.read() == f2.read()

    os.remove(result_output_path)


def test_run_transformation_error():
    files_path = os.path.join("tests", "unit_tests", "files")
    input_path = os.path.join(files_path, "list_buckets_error")
    output_folder_path = os.path.join(files_path)
    expected = RunTransformationSummary(
        **{
            "file_path": "tests/unit_tests/files/list_buckets_error",
            "file_name": "list_buckets_error",
            "status": "FAIL",
            "result_output_path": None,
            "message": "Preprocessor failed to generate appropriate Json format of the response syntax",
        }
    )

    result = run_transformation(input_path, output_folder_path, False)

    assert result == expected
