from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.__fields__.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class Tag(BaseResponse):
    Key: Optional[str]
    Value: Optional[str]


class And(BaseResponse):
    Prefix: Optional[str]
    Tags: Optional[List[Tag]]


class Filter(BaseResponse):
    Prefix: Optional[str]
    Tag: Optional[Tag]
    And: Optional[And]


class S3BucketDestination(BaseResponse):
    Format: Optional[str]
    BucketAccountId: Optional[str]
    Bucket: Optional[str]
    Prefix: Optional[str]


class Destination(BaseResponse):
    S3BucketDestination: Optional[S3BucketDestination]


class DataExport(BaseResponse):
    OutputSchemaVersion: Optional[str]
    Destination: Optional[Destination]


class StorageClassAnalysis(BaseResponse):
    DataExport: Optional[DataExport]


class AnalyticsConfigurationListItem(BaseResponse):
    Id: Optional[str]
    Filter: Optional[Filter]
    StorageClassAnalysis: Optional[StorageClassAnalysis]


class ListBucketAnalyticsConfigurationsResponse(BaseResponse):
    IsTruncated: Optional[bool]
    ContinuationToken: Optional[str]
    NextContinuationToken: Optional[str]
    AnalyticsConfigurationList: Optional[List[AnalyticsConfigurationListItem]]
