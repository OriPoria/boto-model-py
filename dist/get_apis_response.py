from __future__ import annotations
from enum import Enum
from datetime import datetime


class ProtocolType(Enum):
    W_E_B_S_O_C_K_E_T = 'WEBSOCKET'
    H_T_T_P = 'HTTP'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.__fields__.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class CorsConfiguration(BaseResponse):
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[List[str]]
    AllowMethods: Optional[List[str]]
    AllowOrigins: Optional[List[str]]
    ExposeHeaders: Optional[List[str]]
    MaxAge: Optional[int]


class Tags(BaseResponse):
    string: Optional[str]


class Item(BaseResponse):
    ApiEndpoint: Optional[str]
    ApiGatewayManaged: Optional[bool]
    ApiId: Optional[str]
    ApiKeySelectionExpression: Optional[str]
    CorsConfiguration: Optional[CorsConfiguration]
    CreatedDate: Optional[datetime]
    Description: Optional[str]
    DisableSchemaValidation: Optional[bool]
    DisableExecuteApiEndpoint: Optional[bool]
    ImportInfo: Optional[List[str]]
    Name: Optional[str]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[str]
    Tags: Optional[Tags]
    Version: Optional[str]
    Warnings: Optional[List[str]]


class GetApisResponse(BaseResponse):
    Items: Optional[List[Item]]
    NextToken: Optional[str]
