from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class StatusState(Enum):
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'


class EncryptionOption(Enum):
    SSE_S3 = 'SSE_S3'
    SSE_KMS = 'SSE_KMS'
    CSE_KMS = 'CSE_KMS'


class StatementType(Enum):
    DDL = 'DDL'
    DML = 'DML'
    UTILITY = 'UTILITY'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class EncryptionConfiguration(BaseResponse):
    EncryptionOption: Optional[EncryptionOption]
    KmsKey: Optional[str]


class AclConfiguration(BaseResponse):
    S3AclOption: Optional[str]


class ResultConfiguration(BaseResponse):
    OutputLocation: Optional[str]
    EncryptionConfiguration: Optional[EncryptionConfiguration]
    ExpectedBucketOwner: Optional[str]
    AclConfiguration: Optional[AclConfiguration]


class ResultReuseByAgeConfiguration(BaseResponse):
    Enabled: Optional[bool]
    MaxAgeInMinutes: Optional[int]


class ResultReuseConfiguration(BaseResponse):
    ResultReuseByAgeConfiguration: Optional[ResultReuseByAgeConfiguration]


class QueryExecutionContext(BaseResponse):
    Database: Optional[str]
    Catalog: Optional[str]


class AthenaError(BaseResponse):
    ErrorCategory: Optional[int]
    ErrorType: Optional[int]
    Retryable: Optional[bool]
    ErrorMessage: Optional[str]


class Status(BaseResponse):
    State: Optional[StatusState]
    StateChangeReason: Optional[str]
    SubmissionDateTime: Optional[datetime]
    CompletionDateTime: Optional[datetime]
    AthenaError: Optional[AthenaError]


class ResultReuseInformation(BaseResponse):
    ReusedPreviousResult: Optional[bool]


class Statistics(BaseResponse):
    EngineExecutionTimeInMillis: Optional[int]
    DataScannedInBytes: Optional[int]
    DataManifestLocation: Optional[str]
    TotalExecutionTimeInMillis: Optional[int]
    QueryQueueTimeInMillis: Optional[int]
    ServicePreProcessingTimeInMillis: Optional[int]
    QueryPlanningTimeInMillis: Optional[int]
    ServiceProcessingTimeInMillis: Optional[int]
    ResultReuseInformation: Optional[ResultReuseInformation]


class EngineVersion(BaseResponse):
    SelectedEngineVersion: Optional[str]
    EffectiveEngineVersion: Optional[str]


class QueryResultsS3AccessGrantsConfiguration(BaseResponse):
    EnableS3AccessGrants: Optional[bool]
    CreateUserLevelPrefix: Optional[bool]
    AuthenticationType: Optional[str]


class QueryExecution(BaseResponse):
    QueryExecutionId: Optional[str]
    Query: Optional[str]
    StatementType: Optional[StatementType]
    ResultConfiguration: Optional[ResultConfiguration]
    ResultReuseConfiguration: Optional[ResultReuseConfiguration]
    QueryExecutionContext: Optional[QueryExecutionContext]
    Status: Optional[Status]
    Statistics: Optional[Statistics]
    WorkGroup: Optional[str]
    EngineVersion: Optional[EngineVersion]
    ExecutionParameters: Optional[List[str]]
    SubstatementType: Optional[str]
    QueryResultsS3AccessGrantsConfiguration: Optional[
        QueryResultsS3AccessGrantsConfiguration]


class GetQueryExecutionResponse(BaseResponse):
    QueryExecution: Optional[QueryExecution]
