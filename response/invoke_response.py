from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import Optional
from pydantic import BaseModel


class InvokeResponse(BaseResponse):
    StatusCode: Optional[int]
    FunctionError: Optional[str]
    LogResult: Optional[str]
    Payload: Optional[str]
    ExecutedVersion: Optional[str]
