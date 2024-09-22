from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class FailedFinding(BaseResponse):
    Id: Optional[str]
    ErrorCode: Optional[str]
    ErrorMessage: Optional[str]


class BatchImportFindingsResponse(BaseResponse):
    FailedCount: Optional[int]
    SuccessCount: Optional[int]
    FailedFindings: Optional[List[FailedFinding]]
