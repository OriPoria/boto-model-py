import re
import json
from dataclasses import dataclass
from typing import Callable

def replace_one_quote_dict_to_json(string: str) -> str:
    replaced = re.sub(r"'", '"', string)
    return replaced


LINE_OF_BOOLEAN_PREFIX = "BOOL_LINE_NUMBER"
LINE_OF_ENUM_PREFIX = "ENUM_LINE_NUMBER"
LINE_OF_DATETIME_PREFIX = "DATETIME_LINE_NUMBER"

@dataclass
class SpecialType:
    placeholder: str
    predicat: Callable[[str], bool]


datetime_type = SpecialType(placeholder=LINE_OF_DATETIME_PREFIX,
                            predicat=lambda line: "datetime(" in line)

boolean_type = SpecialType(placeholder=LINE_OF_BOOLEAN_PREFIX,
                           predicat=lambda line: "True|False" in line)

def enum_line_prediction(line: str) -> bool:
    enum_token = line.rstrip(",").split("|")
    pattern = r'^".*"$'  # ^- start string, $- end of string
    return len(enum_token) > 1 and bool(re.match(pattern, enum_token[-1]))


enum_type = SpecialType(placeholder=LINE_OF_ENUM_PREFIX,
                        predicat=enum_line_prediction)


def list_keys_and_extract_lines_of_type(string: str, special_type: SpecialType) -> list[str]:
    lines = string.split("\n")
    line_number_with_type = list()
    for i, l in enumerate(lines):
        if special_type.predicat(l):
            line_number_with_type.append(f"{special_type.placeholder}_{i}")
    return line_number_with_type


def replace_line_of_enums(string: str, line_of_enums: list[str]) -> tuple[str, dict]:
    lines = string.split("\n")
    line_numbers = {int(i.split("_")[-1]) for i in line_of_enums}
    enum_map_from_line_number_to_list_of_strings = dict()
    for i, l in enumerate(lines):
        if i in line_numbers:
            line_of_enum_splitted = l.strip(",").split(": ")
            assert len(line_of_enum_splitted) == 2
            part_of_value = line_of_enum_splitted[1]
            list_of_values = part_of_value.split("|")
            enum_map_from_line_number_to_list_of_strings[i] = [v.strip("\"") for v in list_of_values]
            string = string.replace(part_of_value, f"\"{LINE_OF_ENUM_PREFIX}_{i}\"", 1)
    return string, enum_map_from_line_number_to_list_of_strings


def replace_line_of_boolean(string: str, line_of_bool: list[str]) -> str:
    lines = string.split("\n")
    line_numbers = {int(i.split("_")[-1]) for i in line_of_bool}
    line_numbers = sorted(line_numbers)
    for i, l in enumerate(lines):
        if i in line_numbers:
            full_line = l
            line_of_bool_splitted = l.strip(",").split(": ")
            assert len(line_of_bool_splitted) == 2
            part_of_value = line_of_bool_splitted[1]
            full_line_replaced = full_line.replace(part_of_value, f"\"{LINE_OF_BOOLEAN_PREFIX}_{i}\"")
            string = string.replace(full_line, full_line_replaced, 1)
    return string


def replace_line_of_datetime(string: str, line_of_datetime: list[str]) -> str:
    lines = string.split("\n")
    line_numbers = {int(i.split("_")[-1]) for i in line_of_datetime}
    for i, l in enumerate(lines):
        if i in line_numbers:
            full_line = l
            line_of_enum_splitted = l.strip(",").split(": ")
            assert len(line_of_enum_splitted) == 2
            part_of_value = line_of_enum_splitted[1]
            full_line_replaced = full_line.replace(part_of_value, f"\"{LINE_OF_DATETIME_PREFIX}_{i}\"")
            string = string.replace(full_line, full_line_replaced, 1)
    return string


def generate_enum_dicts(string: str, line_numbers_of_enums: set[int]) -> list[tuple]:
    lines = string.split("\n")
    enums_dicts = list()
    for i, l in enumerate(lines):
        if i in line_numbers_of_enums:
            line_of_enum_splitted = l.strip(",").split(": ")
            assert len(line_of_enum_splitted) == 2
            part_of_value = line_of_enum_splitted[1]
            part_of_key = line_of_enum_splitted[0].strip(" ").strip('"')
            enum_values = part_of_value.split("|")
            dict_ = dict()
            for enum_value in enum_values:
                dict_[enum_value.upper().replace("-", "_").strip('"')] = enum_value
            enums_dicts.append((part_of_key, dict_))
    return enums_dicts


def remove_white_spaces(string: str) -> str:
    clean_str = re.sub(r'\s+', '', string)
    return clean_str


def remove_unquoted_commas(text) -> str:
    pattern = re.compile(r'(?<!"),(?!")')
    text = text.replace("\",]", "\"]")
    text = pattern.sub('', text)
    return text

def preprocess_input(string: str) -> tuple[dict, list[str], list[str], list[str], list[tuple], dict]:
    s_ = replace_one_quote_dict_to_json(string)
    lkod = list_keys_and_extract_lines_of_type(s_, datetime_type)
    lkob = list_keys_and_extract_lines_of_type(s_, boolean_type)
    lkwe = list_keys_and_extract_lines_of_type(s_, enum_type)
    enum_dict = generate_enum_dicts(s_, {int(it.split("_")[-1]) for it in lkwe})
    s_, map_from_line_of_enum_to_list_of_values = replace_line_of_enums(s_, lkwe)
    s_ = replace_line_of_boolean(s_, lkob)
    s_ = replace_line_of_datetime(s_, lkod)
    s_ = remove_white_spaces(s_)
    s_ = remove_unquoted_commas(s_)
    dict_json = json.loads(s_)
    return dict_json, lkod, lkob, lkwe, enum_dict, map_from_line_of_enum_to_list_of_values
