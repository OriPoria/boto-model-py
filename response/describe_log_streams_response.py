from __future__ import annotations
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class LogStream(BaseResponse):
    logStreamName: Optional[str]
    creationTime: Optional[int]
    firstEventTimestamp: Optional[int]
    lastEventTimestamp: Optional[int]
    lastIngestionTime: Optional[int]
    uploadSequenceToken: Optional[str]
    arn: Optional[str]
    storedBytes: Optional[int]


class DescribeLogStreamsResponse(BaseResponse):
    logStreams: Optional[List[LogStream]]
    nextToken: Optional[str]
