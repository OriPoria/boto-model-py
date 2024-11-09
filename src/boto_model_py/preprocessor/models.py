from dataclasses import dataclass


@dataclass
class PreprocessedData:
    preprocessed_json: dict
    key_line_datetime: list[str]
    key_line_boolean: list[str]
    key_line_enum: list
    enum_line_values_map: dict
