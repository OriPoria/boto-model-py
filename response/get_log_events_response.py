from __future__ import annotations
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class Event(BaseResponse):
    timestamp: Optional[int]
    message: Optional[str]
    ingestionTime: Optional[int]


class GetLogEventsResponse(BaseResponse):
    events: Optional[List[Event]]
    nextForwardToken: Optional[str]
    nextBackwardToken: Optional[str]
