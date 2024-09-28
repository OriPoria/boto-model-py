from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class code(Enum):
    AWS_SERVICE_ACCESS_DISABLED = 'AWS_SERVICE_ACCESS_DISABLED'
    DELEGATED_ADMINISTRATOR_DEREGISTERED = (
        'DELEGATED_ADMINISTRATOR_DEREGISTERED')
    ORGANIZATION_DELETED = 'ORGANIZATION_DELETED'
    SERVICE_LINKED_ROLE_CREATION_FAILED = 'SERVICE_LINKED_ROLE_CREATION_FAILED'


class status(Enum):
    ACTIVE = 'ACTIVE'
    CREATING = 'CREATING'
    DISABLED = 'DISABLED'
    FAILED = 'FAILED'


class type(Enum):
    ACCOUNT = 'ACCOUNT'
    ORGANIZATION = 'ORGANIZATION'
    ACCOUNT_UNUSED_ACCESS = 'ACCOUNT_UNUSED_ACCESS'
    ORGANIZATION_UNUSED_ACCESS = 'ORGANIZATION_UNUSED_ACCESS'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class Tags(BaseResponse):
    string: Optional[str]


class StatusReason(BaseResponse):
    code: Optional[code]


class UnusedAccess(BaseResponse):
    unusedAccessAge: Optional[int]


class Configuration(BaseResponse):
    unusedAccess: Optional[UnusedAccess]


class Analyzer(BaseResponse):
    arn: Optional[str]
    name: Optional[str]
    type: Optional[type]
    createdAt: Optional[datetime]
    lastResourceAnalyzed: Optional[str]
    lastResourceAnalyzedAt: Optional[datetime]
    tags: Optional[Tags]
    status: Optional[status]
    statusReason: Optional[StatusReason]
    configuration: Optional[Configuration]


class ListAnalyzersResponse(BaseResponse):
    analyzers: Optional[List[Analyzer]]
    nextToken: Optional[str]
