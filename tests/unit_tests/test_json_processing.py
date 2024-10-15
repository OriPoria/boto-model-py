from boto_model_py.json_processing import find_path


def test_find_path():
    dict_json = {
        "person": "Alice"
    }
    path = find_path(dict_json, "Alice")
    assert path == ["person"]


def test_find_path_list():
    dict_json = [
        {
            "name": "Bob"
        },
        {
            "name": "Carol"
        }
    ]
    path = find_path(dict_json, "Carol")
    assert path == ["name"]


def test_find_path_complex():
    dict_json = {
        "person": {
            "name": "Bob",
            "addresses": [
                {
                    "city": "Los Angeles"
                },
                {
                    "city": "New York"
                }
            ]
        }
    }
    path = find_path(dict_json, "Los Angeles")
    assert path == ["person", "addresses", "city"]