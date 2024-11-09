import os

from boto_model_py.preprocessor.preprocessing import SpecialTypeLinesExtractor
from boto_model_py.preprocessor.consts import SpecialTypesNames
from boto_model_py.preprocessor.preprocessing import SpecialTypeLineReplacer
from boto_model_py.preprocessor.preprocessing import StringFormatter
from boto_model_py.preprocessor.preprocessing import build_special_type_string_line
from boto_model_py.preprocessor.consts import SpecialTypeLinePlaceholder
from boto_model_py.preprocessor.preprocessing import replace_one_quote_dict_to_json


def test_special_type_lines_extractor_no_special_types():
    response_syntax_string = 'key1: "value1"\\nkey2: "value2"'
    extractor = SpecialTypeLinesExtractor(response_syntax_string)
    result = extractor.extract_lines_of_types()
    expected_result = {
        SpecialTypesNames.ENUM: [],
        SpecialTypesNames.DATETIME: [],
        SpecialTypesNames.BOOLEAN: [],
        SpecialTypesNames.OBJECT: [],
    }
    assert result, expected_result


def test_special_type_line_replacer_replace_lines_of_enums():
    response_syntax_string = 'key: "option1"|"option2"'
    replacer = SpecialTypeLineReplacer(response_syntax_string)
    result = replacer.replace_lines_of_enums(["ENUM_LINE_NUMBER_0"])
    expected_result = {0: ["option1", "option2"]}
    assert result == expected_result
    assert replacer.processed_string == 'key: "ENUM_LINE_NUMBER_0"'


def test_string_formatter_remove_white_spaces():
    input_string = '  key1: "value1" , key2: "value2"  '
    formatter = StringFormatter(input_string)
    formatter.remove_white_spaces()
    expected_output = 'key1:"value1",key2:"value2"'
    assert formatter.processed_string == expected_output


def test_build_special_type_string_line():
    placeholder = SpecialTypeLinePlaceholder.LINE_OF_ENUM_PREFIX
    line_number = 5
    expected_output = f"{placeholder}_{line_number}"
    assert build_special_type_string_line(placeholder, line_number) == expected_output


def test_replace_one_quote_dict_to_json():
    input_string = "{'key': 'value'}"
    expected_output = '{"key": "value"}'
    assert replace_one_quote_dict_to_json(input_string) == expected_output


def test_special_type_lines_extractor_with_datetime():
    response_syntax_string = 'key1: datetime(2023, 10, 1)\\nkey2: "value2"'
    extractor = SpecialTypeLinesExtractor(response_syntax_string)
    result = extractor.extract_lines_of_types()
    expected_result = {
        SpecialTypesNames.ENUM: [],
        SpecialTypesNames.DATETIME: ["DATETIME_LINE_NUMBER_0"],
        SpecialTypesNames.BOOLEAN: [],
        SpecialTypesNames.OBJECT: [],
    }
    assert result == expected_result


def test_replace_line_of_item():
    line_of_item = ["BOOL_LINE_NUMBER_28"]
    place_holder = SpecialTypeLinePlaceholder.LINE_OF_BOOLEAN_PREFIX
    with open(
        os.path.join("tests", "unit_tests", "files", "response_syntax_string.txt")
    ) as f:
        string_lines = f.read()

    replacer = SpecialTypeLineReplacer(response_syntax_string=string_lines)
    replacer.replace_line_of_item(line_of_item=line_of_item, place_holder=place_holder)

    with open(
        os.path.join(
            "tests", "unit_tests", "files", "response_syntax_string_expected.txt"
        )
    ) as f:
        response_syntax_string_expected = f.read()

    assert response_syntax_string_expected == replacer.response_syntax_string
