import re
import json
from dataclasses import dataclass
from typing import Callable

def replace_one_quote_dict_to_json(string: str) -> str:
    replaced = re.sub(r"'", '"', string)
    return replaced

def alignment(string: str) -> str:
    new_lines = list()
    lines = string.split("\n")
    idx = 0
    while idx < len(lines):
        if lines[idx].endswith("["):
            list_line = lines[idx]
            while True:
                idx += 1
                list_line += lines[idx]
                if "]" in lines[idx]:
                    break
            new_lines.append(list_line)
        else:
            new_lines.append(lines[idx])
        idx += 1
    return "\n".join(new_lines)


LINE_OF_BOOLEAN_PREFIX = "BOOL_LINE_NUMBER"
LINE_OF_ENUM_PREFIX = "ENUM_LINE_NUMBER"
LINE_OF_DATETIME_PREFIX = "DATETIME_LINE_NUMBER"
LINE_OF_OBJECT_PREFIX = "OBJECT_LINE_NUMBER"

@dataclass
class SpecialType:
    placeholder: str
    predicat: Callable[[str], bool]


datetime_type = SpecialType(placeholder=LINE_OF_DATETIME_PREFIX,
                            predicat=lambda line: "datetime(" in line)

boolean_type = SpecialType(placeholder=LINE_OF_BOOLEAN_PREFIX,
                           predicat=lambda line: "True|False" in line)

object_type = SpecialType(placeholder=LINE_OF_OBJECT_PREFIX,
                          predicat=lambda line: "()" in line)

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
    line_numbers = [int(i.split("_")[-1]) for i in line_of_enums]
    numbers_idx = 0
    enum_map_from_line_number_to_list_of_strings = dict()
    i = 0
    while i < len(lines):
        l = lines[i]
        if i in line_numbers:
            line_of_enum_splitted = l.strip(",").split(": ")
            if len(line_of_enum_splitted) == 2:
                part_of_value = line_of_enum_splitted[1]

            elif len(line_of_enum_splitted) == 1:
                part_of_value = lines[i]
                i+=1
            else:
                raise Exception
            list_of_values = part_of_value.split("|")
            enum_map_from_line_number_to_list_of_strings[line_numbers[numbers_idx]] = [v.strip("\"") for v in list_of_values]
            string = string.replace(part_of_value, f"\"{LINE_OF_ENUM_PREFIX}_{line_numbers[numbers_idx]}\"", 1)
            numbers_idx += 1
        i += 1
    return string, enum_map_from_line_number_to_list_of_strings

def replace_line_of_item(string: str, line_of_item: list[str], place_holder: str) -> str:
    """ Can replace of bool, datetime or object """
    lines = string.split("\n")
    line_numbers = {int(i.split("_")[-1]) for i in line_of_item}
    line_numbers = sorted(line_numbers)
    for i, l in enumerate(lines):
        if i in line_numbers:
            full_line = l
            line_of_bool_splitted = l.strip(",").split(": ")
            assert len(line_of_bool_splitted) == 2
            part_of_value = line_of_bool_splitted[1]
            full_line_replaced = full_line.replace(part_of_value, f"\"{place_holder}_{i}\"")
            string = string.replace(full_line, full_line_replaced, 1)
    return string


def generate_enum_dicts(string: str, line_numbers_of_enums: set[int]) -> list[tuple]:
    lines = string.split("\n")
    enums_dicts = list()
    for i, l in enumerate(lines):
        if i in line_numbers_of_enums:
            line_of_enum_split = l.strip(",").split(": ")
            if len(line_of_enum_split) == 2:
                part_of_value = line_of_enum_split[1]
                part_of_key = line_of_enum_split[0].strip(" ").strip('"')
            elif len(line_of_enum_split) == 1 and lines[i-1].endswith("["):
                part_of_value = line_of_enum_split[0]
                matches = re.findall(r'"(.*?)"', lines[i-1])
                assert len(matches) == 1
                part_of_key = matches[0]
            else:
                raise Exception("Unexpected length of enum")
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

@dataclass
class PreprocessedData:
    preprocessed_json: dict
    key_line_datetime: list[str]
    key_line_boolean: list[str]
    key_line_enum: list
    enum_dictionary: list[tuple]
    enum_line_values_map: dict

class PreprocessException(Exception):
    pass


def preprocess_input(string: str) -> PreprocessedData:
    s_ = replace_one_quote_dict_to_json(string)
    lkod = list_keys_and_extract_lines_of_type(s_, datetime_type)
    lkob = list_keys_and_extract_lines_of_type(s_, boolean_type)
    lkwe = list_keys_and_extract_lines_of_type(s_, enum_type)
    lkoo = list_keys_and_extract_lines_of_type(s_, object_type)
    enum_idx = [int(it.split("_")[-1]) for it in lkwe]
    enum_idx.sort()
    enum_dict = generate_enum_dicts(s_, set(enum_idx))

    # Replace input string with placeholder of special types
    s_, map_from_line_of_enum_to_list_of_values = replace_line_of_enums(s_, lkwe)
    s_ = replace_line_of_item(s_, lkob, LINE_OF_BOOLEAN_PREFIX)
    s_ = replace_line_of_item(s_, lkod, LINE_OF_DATETIME_PREFIX)
    s_ = replace_line_of_item(s_, lkoo, LINE_OF_OBJECT_PREFIX)
    s_ = remove_white_spaces(s_)
    s_ = remove_unquoted_commas(s_)
    dict_json = json.loads(s_)
    return PreprocessedData(
        preprocessed_json=dict_json,
        key_line_datetime=lkod,
        key_line_boolean=lkob,
        key_line_enum=lkwe,
        enum_dictionary=enum_dict,
        enum_line_values_map=map_from_line_of_enum_to_list_of_values
    )
