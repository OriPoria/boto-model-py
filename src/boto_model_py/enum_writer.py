import re
import ast
from typing import Optional


WITH_PARENT_NAME = ["State", "Status"]


def get_enum_class_name(dict_json: dict, enum_line_number: str) -> Optional[str]:
    if isinstance(dict_json, str):
        return None
    for k, v in dict_json.items():
        if v == enum_line_number:
            return k
        elif isinstance(v, dict):
            result = get_enum_class_name(v, enum_line_number)
            if result:
                if result in WITH_PARENT_NAME:
                    return k + result
                return result
        elif isinstance(v, list):
            if len(v) == 1 and isinstance(v[0], str) and v[0] == enum_line_number:
                return k
            for item in v:
                result = get_enum_class_name(item, enum_line_number)
                if result:
                    if result in WITH_PARENT_NAME:
                        return k + result
                    return result


def generate_enum_var_name(camel_str: str) -> str:
    camel_str = camel_str.strip()

    def _is_upper_or_number_or_underscore(c: str) -> bool:
        return c.isupper() or c == "_" or c.isdigit()

    if all([_is_upper_or_number_or_underscore(c) for c in camel_str]):
        return camel_str
    else:
        # Use a regular expression to find the positions to insert underscores
        underscore_str = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str)
        # Convert the resulting string to upper case
        upper_str = underscore_str.upper()
        upper_str = re.sub(r"[.-]|::", "", upper_str)

        return upper_str


def write_enum_class(class_name: str, attrs: list[str]) -> str:
    class_str = f"class {class_name}(Enum):\n"
    for a in attrs:
        attr = a.strip().replace('"', "").replace(",", "")
        class_str += f'\t{generate_enum_var_name(attr)} = "{attr}"\n'
    return class_str


def enum_classes_to_replace(
    dict_json: dict,
    map_from_value_of_temp_enum_to_list_of_path: dict,
    map_from_line_of_enum_to_list_of_values: dict,
):
    enum_class_to_replace = dict()
    enum_class_names_to_path = list()
    enum_classes = list()
    enum_classes_names = set()
    for k, v in map_from_value_of_temp_enum_to_list_of_path.items():
        class_name = get_enum_class_name(dict_json, k)
        if class_name in enum_classes_names:
            raise Exception(f"Duplication in enum classes names. Name: {class_name}")
        enum_class_to_replace[k] = class_name
        enum_class_names_to_path.append({class_name: v})
    for k, v in enum_class_to_replace.items():
        enum_classes.append(
            write_enum_class(
                v, map_from_line_of_enum_to_list_of_values[int(k.split("_")[-1])]
            )
        )
    enum_classes_ast_objs = list()
    for e_c in enum_classes:
        enum_classes_ast_objs.append(ast.parse(e_c).body[0])
    if not all([isinstance(c, ast.ClassDef) for c in enum_classes_ast_objs]):
        raise TypeError("Not all classes found of enum are type ast.ClassDef")
    return enum_classes_ast_objs, enum_class_names_to_path
