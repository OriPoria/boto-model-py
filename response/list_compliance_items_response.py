from __future__ import annotations
from enum import Enum
from datetime import datetime


class Severity(Enum):
    CRITICAL = 'CRITICAL'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    INFORMATIONAL = 'INFORMATIONAL'
    UNSPECIFIED = 'UNSPECIFIED'


class ComplianceItemsStatus(Enum):
    COMPLIANT = 'COMPLIANT'
    NON_COMPLIANT = 'NON_COMPLIANT'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class ExecutionSummary(BaseResponse):
    ExecutionTime: Optional[datetime]
    ExecutionId: Optional[str]
    ExecutionType: Optional[str]


class Details(BaseResponse):
    string: Optional[str]


class ComplianceItem(BaseResponse):
    ComplianceType: Optional[str]
    ResourceType: Optional[str]
    ResourceId: Optional[str]
    Id: Optional[str]
    Title: Optional[str]
    Status: Optional[ComplianceItemsStatus]
    Severity: Optional[Severity]
    ExecutionSummary: Optional[ExecutionSummary]
    Details: Optional[Details]


class ListComplianceItemsResponse(BaseResponse):
    ComplianceItems: Optional[List[ComplianceItem]]
    NextToken: Optional[str]
