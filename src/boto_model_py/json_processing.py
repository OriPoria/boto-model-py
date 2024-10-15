from typing import Union, Optional


def find_path(
    json_part: [Union[str, dict, list]], value, path=None
) -> Optional[list[str]]:
    if path is None:
        path = []
    if isinstance(json_part, str):
        return path if json_part == value else None
    if isinstance(json_part, list):
        for item in json_part:
            result = find_path(item, value, path)
            if result:
                return result
    for k, v in json_part.items():
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


def find_all_path_to_value(dict_json: dict, list_of_values_in_json: list[str]) -> dict:
    result = dict()
    for v in list_of_values_in_json:
        result[v] = find_path(json_part=dict_json, value=v)
    return result
