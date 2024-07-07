from __future__ import annotations
from enum import Enum
from datetime import datetime


class Severity(Enum):
    C_R_I_T_I_C_A_L = 'CRITICAL'
    H_I_G_H = 'HIGH'
    M_E_D_I_U_M = 'MEDIUM'
    L_O_W = 'LOW'
    I_N_F_O_R_M_A_T_I_O_N_A_L = 'INFORMATIONAL'
    U_N_S_P_E_C_I_F_I_E_D = 'UNSPECIFIED'


class ComplianceItemsStatus(Enum):
    C_O_M_P_L_I_A_N_T = 'COMPLIANT'
    N_O_N__C_O_M_P_L_I_A_N_T = 'NON_COMPLIANT'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.__fields__.keys()
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
