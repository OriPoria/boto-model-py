import os
import re
import json
import argparse
import subprocess
import ast
import astor

from enum_writer import enum_classes_to_replace


DIST_FOLDER = "dist"


def replace_one_quote_dict_to_json(string: str) -> str:
    replaced = re.sub(r"'", '"', string)
    return replaced

def remove_white_spaces(string: str) -> str:
    clean_str = re.sub(r'\s+', '', string)
    return clean_str


LINE_OF_BOOLEAN_PREFIX = "BOOL_LINE_NUMBER"
LINE_OF_ENUM_PREFIX = "ENUM_LINE_NUMBER"
LINE_OF_DATETIME_PREFIX = "DATETIME_LINE_NUMBER"


def list_keys_of_boolean(string: str) -> list[str]:
    lines = string.split("\n")
    line_number_with_boolean = list()
    for i, l in enumerate(lines):
        if "True|False" in l:
            line_number_with_boolean.append(f"{LINE_OF_BOOLEAN_PREFIX}_{i}")
    return line_number_with_boolean

def list_keys_of_datetime(string: str) -> list[str]:
    lines = string.split("\n")
    line_number_with_boolean = list()
    for i, l in enumerate(lines):
        if "datetime(" in l:
            line_number_with_boolean.append(f"{LINE_OF_DATETIME_PREFIX}_{i}")
    return line_number_with_boolean


def list_keys_with_enum(string: str) -> list[str]:
    lines = string.split("\n")
    line_number_with_enum = list()
    for i, l in enumerate(lines):
        l.rstrip(",")
        enum_token = l.rstrip(",").split("|")
        pattern = r'^".*"$' # ^- start string, $- end of string
        if len(enum_token) > 1 and bool(re.match(pattern, enum_token[-1])):
            line_number_with_enum.append(f"{LINE_OF_ENUM_PREFIX}_{i}")
    return line_number_with_enum


def generate_enum_dicts(string: str, line_numbers_of_enums: set[int]):
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


def remove_unquoted_commas(text):
    pattern = re.compile(r'(?<!"),(?!")')
    text = text.replace("\",]", "\"]")
    text = pattern.sub('', text)
    return text


def find_path(dict_, value, path=None):
    # TODO: change parameter name to input, not necessarily be a dict as termination
    # If value is found in a list, path is not accurate as warning prints says
    if path is None:
        path = []
    if isinstance(dict_, str):
        print("Warning: found path to value inside a list, potentially need to be more specific with path")
        return path if dict_ == value else None
    for k, v in dict_.items():
        current_path = path + [k]
        if v == value:
            return current_path
        elif isinstance(v, dict):
            result = find_path(v, value, current_path)
            if result:
                return result
        elif isinstance(v, list):
            for item in v:
                result = find_path(item, value, current_path)
                if result:
                    return result
    return None

def find_all_path_to_value(dict_json_: dict, list_of_values_in_json: list[str]) -> dict:
    result = dict()
    for v in list_of_values_in_json:
        result[v] = find_path(dict_json_, v)
    return result


def change_ast_field_type(ast_object_, dict_of_values: dict, actual_type: str):
    for list_of_path in dict_of_values.values():
        next_class = main_class_name
        list_of_path.insert(0, main_class_name)
        len_of_path = len(list_of_path)
        for index in range(0, len_of_path-1):
            for node in ast.walk(ast_object_):
                if isinstance(node, ast.ClassDef) and node.name == next_class:
                    next_attribute = list_of_path[index + 1]
                    for class_body_item in node.body:
                        if isinstance(class_body_item, ast.AnnAssign) and class_body_item.target.id == next_attribute:
                            def get_root_type(class_body_item_):
                                if "slice" in class_body_item_.__dict__:
                                    return get_root_type(class_body_item_.slice)
                                else:
                                    assert isinstance(class_body_item_, ast.Name)
                                    return class_body_item_.id
                            next_class = get_root_type(class_body_item.annotation)
                            if next_class == "str":
                                class_body_item.annotation.slice.id = actual_type


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate pydantic base model from boto3 response format")

    # Add arguments
    parser.add_argument('file_path', type=str, help='The path of the file definition')
    parser.add_argument('--with_metadata', action='store_true', help='Add response metadata to object')

    args = parser.parse_args()

    file_path = args.file_path
    with open(file_path) as f:
        s_ = f.read()
    file_name = os.path.basename(file_path)

    s_ = replace_one_quote_dict_to_json(s_)
    lkod = list_keys_of_datetime(s_)
    lkob = list_keys_of_boolean(s_)
    lkwe = list_keys_with_enum(s_)

    enum_dict = generate_enum_dicts(s_, {int(it.split("_")[-1]) for it in lkwe})
    s_, map_from_line_of_enum_to_list_of_values = replace_line_of_enums(s_, lkwe)
    s_ = replace_line_of_boolean(s_, lkob)
    s_ = replace_line_of_datetime(s_, lkod)
    s_ = remove_white_spaces(s_)
    s_ = remove_unquoted_commas(s_)
    dict_json = json.loads(s_)
    map_from_value_of_temp_bool_to_list_of_path = find_all_path_to_value(dict_json, lkob)
    map_from_value_of_temp_enum_to_list_of_path = find_all_path_to_value(dict_json, lkwe)
    map_from_value_of_temp_datetime_to_list_of_path = find_all_path_to_value(dict_json, lkod)

    temp_json_path = "temp.json"
    with open(temp_json_path, "w") as f:
        json.dump(dict_json, f, indent=2)
    enum_classes_ast, enum_class_names = enum_classes_to_replace(dict_json, map_from_value_of_temp_enum_to_list_of_path, map_from_line_of_enum_to_list_of_values)
    ###### End process of json

    module_path = os.path.join(DIST_FOLDER, f"{file_name}_response.py")
    # Example command
    main_class_name = f"{file_name.title().replace('_', '')}Response"
    command = f"datamodel-codegen --input {temp_json_path} --output {module_path} --force-optional --class-name {main_class_name}"
    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    os.remove(temp_json_path)

    ##### Ast processing
    with open(module_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    source_code = source_code.replace(" = None", "")
    source_code = source_code.replace("(BaseModel):", "(BaseResponse):")


    with open("base_response.py", 'r', encoding='utf-8') as file:
        base_response_code = file.read()
    base_response_code_ast = ast.parse(base_response_code).body
    ast_object = ast.parse(source_code)

    for b_r in base_response_code_ast:
        if isinstance(b_r, ast.ImportFrom):
            ast_object.body.insert(1, b_r)
        else:
            ast_object.body.insert(3, b_r)
    if map_from_value_of_temp_datetime_to_list_of_path:
        ast_object.body.insert(1, ast.parse("from datetime import datetime").body[0])
    if map_from_value_of_temp_enum_to_list_of_path:
        ast_object.body.insert(1, ast.parse("from enum import Enum").body[0])

    for e_c in enum_classes_ast:
        ast_object.body.insert(3, e_c)

    change_ast_field_type(ast_object, map_from_value_of_temp_datetime_to_list_of_path, "datetime")
    change_ast_field_type(ast_object, map_from_value_of_temp_bool_to_list_of_path, "bool")
    for enums_name_to_path in enum_class_names:
        change_ast_field_type(ast_object, enums_name_to_path, list(enums_name_to_path.keys())[0])

    if args.with_metadata:
        for node in ast.walk(ast_object):
            if isinstance(node, ast.ClassDef) and node.name == main_class_name:

                node.body.append(ast.parse("ResponseMetadata: Optional[dict]").body[0])
                print(f"Main class name: {node.name}")

    modified_code = astor.to_source(ast_object)
    # Print the modified code
    with open(module_path, 'w') as f:
        f.write(modified_code)
