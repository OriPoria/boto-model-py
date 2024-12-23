from enum import Enum


class SpecialTypesNames(Enum):
    ENUM = "enum"
    OBJECT = "object"
    BOOLEAN = "boolean"
    DATETIME = "datetime"


class SpecialTypeLinePlaceholder(Enum):
    LINE_OF_BOOLEAN_PREFIX = "BOOL_LINE_NUMBER"
    LINE_OF_ENUM_PREFIX = "ENUM_LINE_NUMBER"
    LINE_OF_DATETIME_PREFIX = "DATETIME_LINE_NUMBER"
    LINE_OF_OBJECT_PREFIX = "OBJECT_LINE_NUMBER"
