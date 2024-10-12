import json
import pathlib
import tempfile


def create_temporary_file(preprocessed_json: dict) -> pathlib.Path:
    with tempfile.NamedTemporaryFile(
        suffix=".json", mode="w+", delete=False
    ) as temp_file:
        json.dump(
            preprocessed_json, temp_file
        )  # Write your JSON data to the temporary file
        temp_file.flush()  # Ensure data is written to disk
        temp_file_path = temp_file.name  # Get the file path for further use
    return pathlib.Path(temp_file_path)
