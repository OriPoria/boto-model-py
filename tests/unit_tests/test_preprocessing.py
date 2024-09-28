def test_a():
    a = 1
    assert a

def test_remove_white_spaces():
    from boto_model_py.preprocessing import remove_white_spaces
    input_str = " a b c "
    expected_output = "abc"
    assert remove_white_spaces(input_str) == expected_output


def test_list_keys_and_extract_lines_of_type():
    from boto_model_py.preprocessing import list_keys_and_extract_lines_of_type, datetime_type
    input_str = 'key1: "value1"\ndatetime(2023, 1, 1)\nkey2: "value2"'
    expected_output = ["DATETIME_LINE_NUMBER_1"]
    assert list_keys_and_extract_lines_of_type(input_str, datetime_type) == expected_output


def test_alignment():
    from boto_model_py.preprocessing import alignment
    input_str = "line1\nline2[\nline3\nline4]\nline5"
    expected_output = "line1\nline2[line3line4]\nline5"
    assert alignment(input_str) == expected_output


def test_replace_one_quote_dict_to_json():
    from boto_model_py.preprocessing import replace_one_quote_dict_to_json
    input_str = "{'key': 'value'}"
    expected_output = '{"key": "value"}'
    assert replace_one_quote_dict_to_json(input_str) == expected_output


def test_replace_line_of_item_boolean():
    from boto_model_py.preprocessing import replace_line_of_item, LINE_OF_BOOLEAN_PREFIX
    input_str = 'key1: True\nkey2: False\nkey3: "value3"'
    line_of_item = ["BOOL_LINE_NUMBER_0", "BOOL_LINE_NUMBER_1"]
    expected_output_str = f'key1: "{LINE_OF_BOOLEAN_PREFIX}_0"\nkey2: "{LINE_OF_BOOLEAN_PREFIX}_1"\nkey3: "value3"'
    output_str = replace_line_of_item(input_str, line_of_item, LINE_OF_BOOLEAN_PREFIX)
    assert output_str == expected_output_str


def test_replace_line_of_enums():
    from boto_model_py.preprocessing import replace_line_of_enums
    input_str = 'key1: "value1"\nkey2: "value2|value3"\nkey3: "value4"'
    line_of_enums = ["ENUM_LINE_NUMBER_1"]
    expected_output_str = 'key1: "value1"\nkey2: "ENUM_LINE_NUMBER_1"\nkey3: "value4"'
    expected_enum_map = {1: ["value2", "value3"]}
    output_str, enum_map = replace_line_of_enums(input_str, line_of_enums)
    assert output_str == expected_output_str
    assert enum_map == expected_enum_map


def test_enum_line_prediction():
    from boto_model_py.preprocessing import enum_line_prediction
    input_str = '"value1"|"value2"'
    assert enum_line_prediction(input_str) == True
    input_str = '"value1"'
    assert enum_line_prediction(input_str) == False
