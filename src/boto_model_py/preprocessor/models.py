from dataclasses import dataclass


@dataclass
class PreprocessedData:
    preprocessed_json: dict
    key_line_datetime: dict
    key_line_boolean: dict
    key_line_enum: dict
    enum_line_values_map: dict
