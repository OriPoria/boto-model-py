from boto_model_py.enum_writer import (
    _generate_enum_var_name,
    enum_classes_to_replace,
    write_enum_class,
    get_enum_class_name,
)


def test_generate_enum_var_name_camel():
    res = _generate_enum_var_name("testSet")
    assert res == "TEST_SET"


def test_generate_enum_var_name_all_upper():
    res = _generate_enum_var_name("TEST")
    assert res == "TEST"


def test_get_enum_class_name_with_parent_name_in_list():
    dict_json = {"key1": [{"Status": "enum_line"}]}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "key1Status"


def test_enum_classes_to_replace_duplicate_names():
    dict_json = {"key1": "enum_line_1", "key2": "enum_line_2"}
    map_from_value_of_temp_enum_to_list_of_path = {
        "enum_line_1": ["path1"],
        "enum_line_2": ["path2"],
    }
    map_from_line_of_enum_to_list_of_values = {1: ["value1"], 2: ["value2"]}
    try:
        enum_classes_to_replace(
            dict_json,
            map_from_value_of_temp_enum_to_list_of_path,
            map_from_line_of_enum_to_list_of_values,
        )
    except Exception as e:
        assert str(e) == "Duplication in enum classes names. Name: None"


def test_write_enum_class():
    class_name = "TestEnum"
    attrs = ["attr1", "attr2"]
    result = write_enum_class(class_name, attrs)
    expected = 'class TestEnum(Enum):\n\tATTR1 = "attr1"\n\tATTR2 = "attr2"\n'
    assert result == expected


def test_get_enum_class_name_with_parent_name():
    dict_json = {"key1": {"State": "enum_line"}}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "key1State"


def test_get_enum_class_name_nested_list():
    dict_json = {"key1": [{"nested_key": "enum_line"}]}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "nested_key"


def test_get_enum_class_name_list():
    dict_json = {"key1": ["enum_line"]}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "key1"


def test_get_enum_class_name_nested_dict():
    dict_json = {"key1": {"nested_key": "enum_line"}}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "nested_key"


def test_get_enum_class_name_top_level():
    dict_json = {"key1": "enum_line"}
    result = get_enum_class_name(dict_json, "enum_line")
    assert result == "key1"


def test_get_enum_class_name_with_string_input():
    result = get_enum_class_name("not_a_dict", "enum_line")
    assert result is None
