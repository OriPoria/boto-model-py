from __future__ import annotations
from datetime import datetime
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.__fields__.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class S3OutputUrl(BaseResponse):
    OutputUrl: Optional[str]


class OutputUrl(BaseResponse):
    S3OutputUrl: Optional[S3OutputUrl]


class InstanceAssociationStatusInfo(BaseResponse):
    AssociationId: Optional[str]
    Name: Optional[str]
    DocumentVersion: Optional[str]
    AssociationVersion: Optional[str]
    InstanceId: Optional[str]
    ExecutionDate: Optional[datetime]
    Status: Optional[str]
    DetailedStatus: Optional[str]
    ExecutionSummary: Optional[str]
    ErrorCode: Optional[str]
    OutputUrl: Optional[OutputUrl]
    AssociationName: Optional[str]


class DescribeInstanceAssociationsStatusResponse(BaseResponse):
    InstanceAssociationStatusInfos: Optional[List[
        InstanceAssociationStatusInfo]]
    NextToken: Optional[str]
