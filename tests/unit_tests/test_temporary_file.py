import os
import json

from boto_model_py.temporary_file import create_temporary_file


def test_create_temporary_file():
    data = {"name": "abc", "age": 11}

    temp_file_path = create_temporary_file(data)

    with open(temp_file_path) as f:
        file_data = json.load(f)
    assert data == file_data

    os.remove(temp_file_path)
