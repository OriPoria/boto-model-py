from __future__ import annotations
from enum import Enum
from datetime import datetime


class encryptionType(Enum):
    AES256 = 'AES256'
    KMS = 'KMS'


class imageTagMutability(Enum):
    MUTABLE = 'MUTABLE'
    IMMUTABLE = 'IMMUTABLE'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class ImageScanningConfiguration(BaseResponse):
    scanOnPush: Optional[bool]


class EncryptionConfiguration(BaseResponse):
    encryptionType: Optional[encryptionType]
    kmsKey: Optional[str]


class Repository(BaseResponse):
    repositoryArn: Optional[str]
    registryId: Optional[str]
    repositoryName: Optional[str]
    repositoryUri: Optional[str]
    createdAt: Optional[datetime]
    imageTagMutability: Optional[imageTagMutability]
    imageScanningConfiguration: Optional[ImageScanningConfiguration]
    encryptionConfiguration: Optional[EncryptionConfiguration]


class DescribeRepositoriesResponse(BaseResponse):
    repositories: Optional[List[Repository]]
    nextToken: Optional[str]
