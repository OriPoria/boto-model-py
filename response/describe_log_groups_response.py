from __future__ import annotations
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class logGroupClass(Enum):
    STANDARD = 'STANDARD'
    INFREQUENT_ACCESS = 'INFREQUENT_ACCESS'


class dataProtectionStatus(Enum):
    ACTIVATED = 'ACTIVATED'
    DELETED = 'DELETED'
    ARCHIVED = 'ARCHIVED'
    DISABLED = 'DISABLED'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class LogGroup(BaseResponse):
    logGroupName: Optional[str]
    creationTime: Optional[int]
    retentionInDays: Optional[int]
    metricFilterCount: Optional[int]
    arn: Optional[str]
    storedBytes: Optional[int]
    kmsKeyId: Optional[str]
    dataProtectionStatus: Optional[dataProtectionStatus]
    inheritedProperties: Optional[List[str]]
    logGroupClass: Optional[logGroupClass]
    logGroupArn: Optional[str]


class DescribeLogGroupsResponse(BaseResponse):
    logGroups: Optional[List[LogGroup]]
    nextToken: Optional[str]
