from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class AdditionalConfigurationStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class Name(Enum):
    EKS_ADDON_MANAGEMENT = 'EKS_ADDON_MANAGEMENT'
    ECS_FARGATE_AGENT_MANAGEMENT = 'ECS_FARGATE_AGENT_MANAGEMENT'
    EC2_AGENT_MANAGEMENT = 'EC2_AGENT_MANAGEMENT'


class FeaturesStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class Name(Enum):
    FLOW_LOGS = 'FLOW_LOGS'
    CLOUD_TRAIL = 'CLOUD_TRAIL'
    DNS_LOGS = 'DNS_LOGS'
    S3_DATA_EVENTS = 'S3_DATA_EVENTS'
    EKS_AUDIT_LOGS = 'EKS_AUDIT_LOGS'
    EBS_MALWARE_PROTECTION = 'EBS_MALWARE_PROTECTION'
    RDS_LOGIN_EVENTS = 'RDS_LOGIN_EVENTS'
    EKS_RUNTIME_MONITORING = 'EKS_RUNTIME_MONITORING'
    LAMBDA_NETWORK_LOGS = 'LAMBDA_NETWORK_LOGS'
    RUNTIME_MONITORING = 'RUNTIME_MONITORING'


class EbsVolumesStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class AuditLogsStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class S3LogsStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class FlowLogsStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class DNSLogsStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class CloudTrailStatus(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class Status(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


class FindingPublishingFrequency(Enum):
    FIFTEEN_MINUTES = 'FIFTEEN_MINUTES'
    ONE_HOUR = 'ONE_HOUR'
    SIX_HOURS = 'SIX_HOURS'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class CloudTrail(BaseResponse):
    Status: Optional[CloudTrailStatus]


class DNSLogs(BaseResponse):
    Status: Optional[DNSLogsStatus]


class FlowLogs(BaseResponse):
    Status: Optional[FlowLogsStatus]


class S3Logs(BaseResponse):
    Status: Optional[S3LogsStatus]


class AuditLogs(BaseResponse):
    Status: Optional[AuditLogsStatus]


class Kubernetes(BaseResponse):
    AuditLogs: Optional[AuditLogs]


class EbsVolumes(BaseResponse):
    Status: Optional[EbsVolumesStatus]
    Reason: Optional[str]


class ScanEc2InstanceWithFindings(BaseResponse):
    EbsVolumes: Optional[EbsVolumes]


class MalwareProtection(BaseResponse):
    ScanEc2InstanceWithFindings: Optional[ScanEc2InstanceWithFindings]
    ServiceRole: Optional[str]


class DataSources(BaseResponse):
    CloudTrail: Optional[CloudTrail]
    DNSLogs: Optional[DNSLogs]
    FlowLogs: Optional[FlowLogs]
    S3Logs: Optional[S3Logs]
    Kubernetes: Optional[Kubernetes]
    MalwareProtection: Optional[MalwareProtection]


class Tags(BaseResponse):
    string: Optional[str]


class AdditionalConfigurationItem(BaseResponse):
    Name: Optional[Name]
    Status: Optional[AdditionalConfigurationStatus]
    UpdatedAt: Optional[datetime]


class Feature(BaseResponse):
    Name: Optional[Name]
    Status: Optional[FeaturesStatus]
    UpdatedAt: Optional[datetime]
    AdditionalConfiguration: Optional[List[AdditionalConfigurationItem]]


class GetDetectorResponse(BaseResponse):
    CreatedAt: Optional[str]
    FindingPublishingFrequency: Optional[FindingPublishingFrequency]
    ServiceRole: Optional[str]
    Status: Optional[Status]
    UpdatedAt: Optional[str]
    DataSources: Optional[DataSources]
    Tags: Optional[Tags]
    Features: Optional[List[Feature]]
