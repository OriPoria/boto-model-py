from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class ProtocolType(Enum):
    WEBSOCKET = 'WEBSOCKET'
    HTTP = 'HTTP'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


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
