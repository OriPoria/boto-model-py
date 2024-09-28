from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class Type(Enum):
    STRING = 'String'
    STRING_LIST = 'StringList'
    SECURE_STRING = 'SecureString'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class Parameter(BaseResponse):
    Name: Optional[str]
    Type: Optional[Type]
    Value: Optional[str]
    Version: Optional[int]
    Selector: Optional[str]
    SourceResult: Optional[str]
    LastModifiedDate: Optional[datetime]
    ARN: Optional[str]
    DataType: Optional[str]


class GetParametersResponse(BaseResponse):
    Parameters: Optional[List[Parameter]]
    InvalidParameters: Optional[List[str]]
