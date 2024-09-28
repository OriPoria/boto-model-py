from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class type(Enum):
    POLICY = 'POLICY'
    BUCKET_ACL = 'BUCKET_ACL'
    S3_ACCESS_POINT = 'S3_ACCESS_POINT'
    S3_ACCESS_POINT_ACCOUNT = 'S3_ACCESS_POINT_ACCOUNT'


class status(Enum):
    ACTIVE = 'ACTIVE'
    ARCHIVED = 'ARCHIVED'
    RESOLVED = 'RESOLVED'


class resourceType(Enum):
    A_W_S_S3_BUCKET = 'AWS::S3::Bucket'
    A_W_S_I_A_M_ROLE = 'AWS::IAM::Role'
    A_W_S_S_Q_S_QUEUE = 'AWS::SQS::Queue'
    A_W_S_LAMBDA_FUNCTION = 'AWS::Lambda::Function'
    A_W_S_LAMBDA_LAYER_VERSION = 'AWS::Lambda::LayerVersion'
    A_W_S_K_M_S_KEY = 'AWS::KMS::Key'
    A_W_S_SECRETS_MANAGER_SECRET = 'AWS::SecretsManager::Secret'
    A_W_S_E_F_S_FILE_SYSTEM = 'AWS::EFS::FileSystem'
    A_W_S_E_C2_SNAPSHOT = 'AWS::EC2::Snapshot'
    A_W_S_E_C_R_REPOSITORY = 'AWS::ECR::Repository'
    A_W_S_R_D_S_D_B_SNAPSHOT = 'AWS::RDS::DBSnapshot'
    A_W_S_R_D_S_D_B_CLUSTER_SNAPSHOT = 'AWS::RDS::DBClusterSnapshot'
    A_W_S_S_N_S_TOPIC = 'AWS::SNS::Topic'
    A_W_S_S3_EXPRESS_DIRECTORY_BUCKET = 'AWS::S3Express::DirectoryBucket'
    A_W_S_DYNAMO_D_B_TABLE = 'AWS::DynamoDB::Table'
    A_W_S_DYNAMO_D_B_STREAM = 'AWS::DynamoDB::Stream'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class Principal(BaseResponse):
    string: Optional[str]


class Condition(BaseResponse):
    string: Optional[str]


class Detail(BaseResponse):
    accessPointArn: Optional[str]
    accessPointAccount: Optional[str]


class Source(BaseResponse):
    type: Optional[type]
    detail: Optional[Detail]


class Finding(BaseResponse):
    id: Optional[str]
    principal: Optional[Principal]
    action: Optional[List[str]]
    resource: Optional[str]
    isPublic: Optional[bool]
    resourceType: Optional[resourceType]
    condition: Optional[Condition]
    createdAt: Optional[datetime]
    analyzedAt: Optional[datetime]
    updatedAt: Optional[datetime]
    status: Optional[status]
    resourceOwnerAccount: Optional[str]
    error: Optional[str]
    sources: Optional[List[Source]]


class ListFindingsResponse(BaseResponse):
    findings: Optional[List[Finding]]
    nextToken: Optional[str]
