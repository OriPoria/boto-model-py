import re
import json
from dataclasses import dataclass
from typing import Callable, Protocol

from .consts import SpecialTypeLinePlaceholder, SpecialTypesNames

PLACEHOLDER_LINE_NUMBER_SEP = "_"


@dataclass
class SpecialType:
    placeholder: SpecialTypeLinePlaceholder
    predicate: Callable[[str], bool]


datetime_type = SpecialType(
    placeholder=SpecialTypeLinePlaceholder.LINE_OF_DATETIME_PREFIX,
    predicate=lambda line: "datetime(" in line,
)

boolean_type = SpecialType(
    placeholder=SpecialTypeLinePlaceholder.LINE_OF_BOOLEAN_PREFIX,
    predicate=lambda line: "True|False" in line,
)

object_type = SpecialType(
    placeholder=SpecialTypeLinePlaceholder.LINE_OF_OBJECT_PREFIX,
    predicate=lambda line: "()" in line,
)


def enum_line_prediction(line: str) -> bool:
    enum_token = line.rstrip(",").split("|")
    pattern = r'^".*"$'  # ^- start string, $- end of string
    return len(enum_token) > 1 and bool(re.match(pattern, enum_token[-1]))


enum_type = SpecialType(
    placeholder=SpecialTypeLinePlaceholder.LINE_OF_ENUM_PREFIX,
    predicate=enum_line_prediction,
)

type_name_object = {
    SpecialTypesNames.ENUM: enum_type,
    SpecialTypesNames.OBJECT: object_type,
    SpecialTypesNames.BOOLEAN: boolean_type,
    SpecialTypesNames.DATETIME: datetime_type,
}


def replace_one_quote_dict_to_json(string: str) -> str:
    replaced = re.sub(r"'", '"', string)
    return replaced


def build_special_type_string_line(
    placeholder: SpecialTypeLinePlaceholder, line_number: int
) -> str:
    return placeholder + PLACEHOLDER_LINE_NUMBER_SEP + str(line_number)


class SpecialTypeLinesExtractor:

    def __init__(self, response_syntax_string: str):
        self.string_lines = response_syntax_string.split("\n")

    def _list_keys_and_extract_lines_of_type(
        self, special_type: SpecialType
    ) -> list[str]:
        line_number_with_type = list()
        for i, l in enumerate(self.string_lines):
            if special_type.predicate(l):
                line_number_with_type.append(
                    build_special_type_string_line(special_type.placeholder, i)
                )
        return line_number_with_type

    def extract_lines_of_types(self) -> dict[SpecialTypesNames, list[str]]:
        type_name_lines_number_mapping = dict()
        for type_ in SpecialTypesNames:
            type_ = SpecialTypesNames(type_)
            type_name_lines_number_mapping[type_] = (
                self._list_keys_and_extract_lines_of_type(type_name_object[type_])
            )
        return type_name_lines_number_mapping


class StringProcessor(Protocol):

    @property
    def processed_string(self) -> str:
        raise NotImplementedError(
            "Protocol class to mark classes as string processing object"
        )


class SpecialTypeLineReplacer(StringProcessor):

    def __init__(self, response_syntax_string: str):
        self.response_syntax_string = response_syntax_string
        self.string_lines = response_syntax_string.split("\n")

    def replace_lines_of_enums(self, line_of_enums: list[str]):
        line_numbers = [
            int(i.split(PLACEHOLDER_LINE_NUMBER_SEP)[-1]) for i in line_of_enums
        ]
        numbers_idx = 0
        enum_map_from_line_number_to_list_of_strings = dict()
        i = 0
        while i < len(self.string_lines):
            l = self.string_lines[i]
            if i in line_numbers:
                line_of_enum_splitted = l.strip(",").split(": ")
                if len(line_of_enum_splitted) == 2:
                    part_of_value = line_of_enum_splitted[1]

                elif len(line_of_enum_splitted) == 1:
                    part_of_value = self.string_lines[i]
                    i += 1
                else:
                    raise Exception
                list_of_values = part_of_value.split("|")
                enum_map_from_line_number_to_list_of_strings[
                    line_numbers[numbers_idx]
                ] = [v.strip('"') for v in list_of_values]
                self.response_syntax_string = self.response_syntax_string.replace(
                    part_of_value,
                    f'"{SpecialTypeLinePlaceholder.LINE_OF_ENUM_PREFIX}_{line_numbers[numbers_idx]}"',
                    1,
                )
                numbers_idx += 1
            i += 1
        return enum_map_from_line_number_to_list_of_strings

    def replace_line_of_item(self, line_of_item: list[str], place_holder: str):
        """Can replace of bool, datetime or object"""
        line_numbers = {
            int(i.split(PLACEHOLDER_LINE_NUMBER_SEP)[-1]) for i in line_of_item
        }
        line_numbers = sorted(line_numbers)
        for i, l in enumerate(self.string_lines):
            if i in line_numbers:
                full_line = l
                line_of_bool_splitted = l.strip(",").split(": ")
                if len(line_of_bool_splitted) != 2:
                    raise PreprocessException("")
                part_of_value = line_of_bool_splitted[1]
                full_line_replaced = full_line.replace(
                    part_of_value, f'"{place_holder}_{i}"'
                )
                self.response_syntax_string = self.response_syntax_string.replace(
                    full_line, full_line_replaced, 1
                )

    @property
    def processed_string(self) -> str:
        return self.response_syntax_string


def generate_enum_dicts(string: str, line_numbers_of_enums: set[int]) -> list[tuple]:
    lines = string.split("\n")
    enums_dicts = list()
    for i, l in enumerate(lines):
        if i in line_numbers_of_enums:
            line_of_enum_split = l.strip(",").split(": ")
            if len(line_of_enum_split) == 2:
                part_of_value = line_of_enum_split[1]
                part_of_key = line_of_enum_split[0].strip(" ").strip('"')
            elif len(line_of_enum_split) == 1 and lines[i - 1].endswith("["):
                part_of_value = line_of_enum_split[0]
                matches = re.findall(r'"(.*?)"', lines[i - 1])
                assert len(matches) == 1
                part_of_key = matches[0]
            else:
                raise Exception("Unexpected length of enum")
            enum_values = part_of_value.split("|")
            dict_ = dict()
            for enum_value in enum_values:
                dict_[
                    enum_value.upper()
                    .replace("-", PLACEHOLDER_LINE_NUMBER_SEP)
                    .strip('"')
                ] = enum_value
            enums_dicts.append((part_of_key, dict_))
    return enums_dicts


class StringFormatter(StringProcessor):

    def __init__(self, input_string):
        self.input_string = input_string

    def remove_white_spaces(self):
        self.input_string = re.sub(r"\s+", "", self.input_string)

    def remove_unquoted_commas(self):
        pattern = re.compile(r'(?<!"),(?!")')
        self.input_string = self.input_string.replace('",]', '"]')
        self.input_string = pattern.sub("", self.input_string)

    @property
    def processed_string(self) -> str:
        return self.input_string


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


def preprocess_input(response_syntax_string: str) -> PreprocessedData:
    response_syntax_string = replace_one_quote_dict_to_json(response_syntax_string)
    special_type_lines = SpecialTypeLinesExtractor(
        response_syntax_string
    ).extract_lines_of_types()
    enum_idx = [
        int(it.split(PLACEHOLDER_LINE_NUMBER_SEP)[-1])
        for it in special_type_lines[SpecialTypesNames.ENUM]
    ]
    enum_idx.sort()
    enum_dict = generate_enum_dicts(response_syntax_string, set(enum_idx))

    # Replace input string with placeholder of special types
    string_replacer = SpecialTypeLineReplacer(response_syntax_string)
    map_from_line_of_enum_to_list_of_values = string_replacer.replace_lines_of_enums(
        special_type_lines[SpecialTypesNames.ENUM]
    )
    string_replacer.replace_line_of_item(
        special_type_lines[SpecialTypesNames.BOOLEAN],
        SpecialTypeLinePlaceholder.LINE_OF_BOOLEAN_PREFIX,
    )
    string_replacer.replace_line_of_item(
        special_type_lines[SpecialTypesNames.DATETIME],
        SpecialTypeLinePlaceholder.LINE_OF_DATETIME_PREFIX,
    )
    string_replacer.replace_line_of_item(
        special_type_lines[SpecialTypesNames.OBJECT],
        SpecialTypeLinePlaceholder.LINE_OF_OBJECT_PREFIX,
    )

    string_formatter = StringFormatter(string_replacer.processed_string)

    string_formatter.remove_white_spaces()
    string_formatter.remove_unquoted_commas()
    response_syntax_dict = json.loads(string_formatter.processed_string)
    return PreprocessedData(
        preprocessed_json=response_syntax_dict,
        key_line_datetime=special_type_lines[SpecialTypesNames.DATETIME],
        key_line_boolean=special_type_lines[SpecialTypesNames.BOOLEAN],
        key_line_enum=special_type_lines[SpecialTypesNames.ENUM],
        enum_dictionary=enum_dict,
        enum_line_values_map=map_from_line_of_enum_to_list_of_values,
    )
