from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class status(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETE = 'COMPLETE'
    FAILED = 'FAILED'
    UNSUPPORTED_IMAGE = 'UNSUPPORTED_IMAGE'
    ACTIVE = 'ACTIVE'
    PENDING = 'PENDING'
    SCAN_ELIGIBILITY_EXPIRED = 'SCAN_ELIGIBILITY_EXPIRED'
    FINDINGS_UNAVAILABLE = 'FINDINGS_UNAVAILABLE'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class ImageScanStatus(BaseResponse):
    status: Optional[status]
    description: Optional[str]


class FindingSeverityCounts(BaseResponse):
    string: Optional[int]


class ImageScanFindingsSummary(BaseResponse):
    imageScanCompletedAt: Optional[datetime]
    vulnerabilitySourceUpdatedAt: Optional[datetime]
    findingSeverityCounts: Optional[FindingSeverityCounts]


class ImageDetail(BaseResponse):
    registryId: Optional[str]
    repositoryName: Optional[str]
    imageDigest: Optional[str]
    imageTags: Optional[List[str]]
    imageSizeInBytes: Optional[int]
    imagePushedAt: Optional[datetime]
    imageScanStatus: Optional[ImageScanStatus]
    imageScanFindingsSummary: Optional[ImageScanFindingsSummary]
    imageManifestMediaType: Optional[str]
    artifactMediaType: Optional[str]
    lastRecordedPullTime: Optional[datetime]


class DescribeImagesResponse(BaseResponse):
    imageDetails: Optional[List[ImageDetail]]
    nextToken: Optional[str]
