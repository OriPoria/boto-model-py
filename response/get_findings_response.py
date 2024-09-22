from __future__ import annotations
from enum import Enum
from datetime import datetime


class ProfileSubtype(Enum):
    FREQUENT = 'FREQUENT'
    INFREQUENT = 'INFREQUENT'
    UNSEEN = 'UNSEEN'
    RARE = 'RARE'


class ProfileSubtype(Enum):
    FREQUENT = 'FREQUENT'
    INFREQUENT = 'INFREQUENT'
    UNSEEN = 'UNSEEN'
    RARE = 'RARE'


class ScanType(Enum):
    GUARDDUTY_INITIATED = 'GUARDDUTY_INITIATED'
    ON_DEMAND = 'ON_DEMAND'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class AccessKeyDetails(BaseResponse):
    AccessKeyId: Optional[str]
    PrincipalId: Optional[str]
    UserName: Optional[str]
    UserType: Optional[str]


class Owner(BaseResponse):
    Id: Optional[str]


class Tag(BaseResponse):
    Key: Optional[str]
    Value: Optional[str]


class DefaultServerSideEncryption(BaseResponse):
    EncryptionType: Optional[str]
    KmsMasterKeyArn: Optional[str]


class AccessControlList(BaseResponse):
    AllowsPublicReadAccess: Optional[bool]
    AllowsPublicWriteAccess: Optional[bool]


class BucketPolicy(BaseResponse):
    AllowsPublicReadAccess: Optional[bool]
    AllowsPublicWriteAccess: Optional[bool]


class BlockPublicAccess(BaseResponse):
    IgnorePublicAcls: Optional[bool]
    RestrictPublicBuckets: Optional[bool]
    BlockPublicAcls: Optional[bool]
    BlockPublicPolicy: Optional[bool]


class BucketLevelPermissions(BaseResponse):
    AccessControlList: Optional[AccessControlList]
    BucketPolicy: Optional[BucketPolicy]
    BlockPublicAccess: Optional[BlockPublicAccess]


class AccountLevelPermissions(BaseResponse):
    BlockPublicAccess: Optional[BlockPublicAccess]


class PermissionConfiguration(BaseResponse):
    BucketLevelPermissions: Optional[BucketLevelPermissions]
    AccountLevelPermissions: Optional[AccountLevelPermissions]


class PublicAccess(BaseResponse):
    PermissionConfiguration: Optional[PermissionConfiguration]
    EffectivePermission: Optional[str]


class S3ObjectDetail(BaseResponse):
    ObjectArn: Optional[str]
    Key: Optional[str]
    ETag: Optional[str]
    Hash: Optional[str]
    VersionId: Optional[str]


class S3BucketDetail(BaseResponse):
    Arn: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    CreatedAt: Optional[datetime]
    Owner: Optional[Owner]
    Tags: Optional[List[Tag]]
    DefaultServerSideEncryption: Optional[DefaultServerSideEncryption]
    PublicAccess: Optional[PublicAccess]
    S3ObjectDetails: Optional[List[S3ObjectDetail]]


class IamInstanceProfile(BaseResponse):
    Arn: Optional[str]
    Id: Optional[str]


class PrivateIpAddress(BaseResponse):
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]


class SecurityGroup(BaseResponse):
    GroupId: Optional[str]
    GroupName: Optional[str]


class NetworkInterface(BaseResponse):
    Ipv6Addresses: Optional[List[str]]
    NetworkInterfaceId: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[List[PrivateIpAddress]]
    PublicDnsName: Optional[str]
    PublicIp: Optional[str]
    SecurityGroups: Optional[List[SecurityGroup]]
    SubnetId: Optional[str]
    VpcId: Optional[str]


class ProductCode(BaseResponse):
    Code: Optional[str]
    ProductType: Optional[str]


class InstanceDetails(BaseResponse):
    AvailabilityZone: Optional[str]
    IamInstanceProfile: Optional[IamInstanceProfile]
    ImageDescription: Optional[str]
    ImageId: Optional[str]
    InstanceId: Optional[str]
    InstanceState: Optional[str]
    InstanceType: Optional[str]
    OutpostArn: Optional[str]
    LaunchTime: Optional[str]
    NetworkInterfaces: Optional[List[NetworkInterface]]
    Platform: Optional[str]
    ProductCodes: Optional[List[ProductCode]]
    Tags: Optional[List[Tag]]


class EksClusterDetails(BaseResponse):
    Name: Optional[str]
    Arn: Optional[str]
    VpcId: Optional[str]
    Status: Optional[str]
    Tags: Optional[List[Tag]]
    CreatedAt: Optional[datetime]


class ImpersonatedUser(BaseResponse):
    Username: Optional[str]
    Groups: Optional[List[str]]


class KubernetesUserDetails(BaseResponse):
    Username: Optional[str]
    Uid: Optional[str]
    Groups: Optional[List[str]]
    SessionName: Optional[List[str]]
    ImpersonatedUser: Optional[ImpersonatedUser]


class VolumeMount(BaseResponse):
    Name: Optional[str]
    MountPath: Optional[str]


class SecurityContext(BaseResponse):
    Privileged: Optional[bool]
    AllowPrivilegeEscalation: Optional[bool]


class Container(BaseResponse):
    ContainerRuntime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Image: Optional[str]
    ImagePrefix: Optional[str]
    VolumeMounts: Optional[List[VolumeMount]]
    SecurityContext: Optional[SecurityContext]


class HostPath(BaseResponse):
    Path: Optional[str]


class Volume(BaseResponse):
    Name: Optional[str]
    HostPath: Optional[HostPath]


class KubernetesWorkloadDetails(BaseResponse):
    Name: Optional[str]
    Type: Optional[str]
    Uid: Optional[str]
    Namespace: Optional[str]
    HostNetwork: Optional[bool]
    Containers: Optional[List[Container]]
    Volumes: Optional[List[Volume]]
    ServiceAccountName: Optional[str]
    HostIPC: Optional[bool]
    HostPID: Optional[bool]


class KubernetesDetails(BaseResponse):
    KubernetesUserDetails: Optional[KubernetesUserDetails]
    KubernetesWorkloadDetails: Optional[KubernetesWorkloadDetails]


class ScannedVolumeDetail(BaseResponse):
    VolumeArn: Optional[str]
    VolumeType: Optional[str]
    DeviceName: Optional[str]
    VolumeSizeInGB: Optional[int]
    EncryptionType: Optional[str]
    SnapshotArn: Optional[str]
    KmsKeyArn: Optional[str]


class SkippedVolumeDetail(BaseResponse):
    VolumeArn: Optional[str]
    VolumeType: Optional[str]
    DeviceName: Optional[str]
    VolumeSizeInGB: Optional[int]
    EncryptionType: Optional[str]
    SnapshotArn: Optional[str]
    KmsKeyArn: Optional[str]


class EbsVolumeDetails(BaseResponse):
    ScannedVolumeDetails: Optional[List[ScannedVolumeDetail]]
    SkippedVolumeDetails: Optional[List[SkippedVolumeDetail]]


class Volume1(BaseResponse):
    Name: Optional[str]
    HostPath: Optional[HostPath]


class Container1(BaseResponse):
    ContainerRuntime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Image: Optional[str]
    ImagePrefix: Optional[str]
    VolumeMounts: Optional[List[VolumeMount]]
    SecurityContext: Optional[SecurityContext]


class TaskDetails(BaseResponse):
    Arn: Optional[str]
    DefinitionArn: Optional[str]
    Version: Optional[str]
    TaskCreatedAt: Optional[datetime]
    StartedAt: Optional[datetime]
    StartedBy: Optional[str]
    Tags: Optional[List[Tag]]
    Volumes: Optional[List[Volume1]]
    Containers: Optional[List[Container1]]
    Group: Optional[str]


class EcsClusterDetails(BaseResponse):
    Name: Optional[str]
    Arn: Optional[str]
    Status: Optional[str]
    ActiveServicesCount: Optional[int]
    RegisteredContainerInstancesCount: Optional[int]
    RunningTasksCount: Optional[int]
    Tags: Optional[List[Tag]]
    TaskDetails: Optional[TaskDetails]


class ContainerDetails(BaseResponse):
    ContainerRuntime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Image: Optional[str]
    ImagePrefix: Optional[str]
    VolumeMounts: Optional[List[VolumeMount]]
    SecurityContext: Optional[SecurityContext]


class RdsDbInstanceDetails(BaseResponse):
    DbInstanceIdentifier: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    DbClusterIdentifier: Optional[str]
    DbInstanceArn: Optional[str]
    Tags: Optional[List[Tag]]


class RdsDbUserDetails(BaseResponse):
    User: Optional[str]
    Application: Optional[str]
    Database: Optional[str]
    Ssl: Optional[str]
    AuthMethod: Optional[str]


class VpcConfig(BaseResponse):
    SubnetIds: Optional[List[str]]
    VpcId: Optional[str]
    SecurityGroups: Optional[List[SecurityGroup]]


class LambdaDetails(BaseResponse):
    FunctionArn: Optional[str]
    FunctionName: Optional[str]
    Description: Optional[str]
    LastModifiedAt: Optional[datetime]
    RevisionId: Optional[str]
    FunctionVersion: Optional[str]
    Role: Optional[str]
    VpcConfig: Optional[VpcConfig]
    Tags: Optional[List[Tag]]


class Resource(BaseResponse):
    AccessKeyDetails: Optional[AccessKeyDetails]
    S3BucketDetails: Optional[List[S3BucketDetail]]
    InstanceDetails: Optional[InstanceDetails]
    EksClusterDetails: Optional[EksClusterDetails]
    KubernetesDetails: Optional[KubernetesDetails]
    ResourceType: Optional[str]
    EbsVolumeDetails: Optional[EbsVolumeDetails]
    EcsClusterDetails: Optional[EcsClusterDetails]
    ContainerDetails: Optional[ContainerDetails]
    RdsDbInstanceDetails: Optional[RdsDbInstanceDetails]
    RdsDbUserDetails: Optional[RdsDbUserDetails]
    LambdaDetails: Optional[LambdaDetails]


class DomainDetails(BaseResponse):
    Domain: Optional[str]


class City(BaseResponse):
    CityName: Optional[str]


class Country(BaseResponse):
    CountryCode: Optional[str]
    CountryName: Optional[str]


class GeoLocation(BaseResponse):
    Lat: Optional[float]
    Lon: Optional[float]


class Organization(BaseResponse):
    Asn: Optional[str]
    AsnOrg: Optional[str]
    Isp: Optional[str]
    Org: Optional[str]


class RemoteIpDetails(BaseResponse):
    City: Optional[City]
    Country: Optional[Country]
    GeoLocation: Optional[GeoLocation]
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]
    Organization: Optional[Organization]


class RemoteAccountDetails(BaseResponse):
    AccountId: Optional[str]
    Affiliated: Optional[bool]


class AffectedResources(BaseResponse):
    string: Optional[str]


class AwsApiCallAction(BaseResponse):
    Api: Optional[str]
    CallerType: Optional[str]
    DomainDetails: Optional[DomainDetails]
    ErrorCode: Optional[str]
    UserAgent: Optional[str]
    RemoteIpDetails: Optional[RemoteIpDetails]
    ServiceName: Optional[str]
    RemoteAccountDetails: Optional[RemoteAccountDetails]
    AffectedResources: Optional[AffectedResources]


class DnsRequestAction(BaseResponse):
    Domain: Optional[str]
    Protocol: Optional[str]
    Blocked: Optional[bool]
    DomainWithSuffix: Optional[str]


class LocalPortDetails(BaseResponse):
    Port: Optional[int]
    PortName: Optional[str]


class LocalIpDetails(BaseResponse):
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]


class RemoteIpDetails1(BaseResponse):
    City: Optional[City]
    Country: Optional[Country]
    GeoLocation: Optional[GeoLocation]
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]
    Organization: Optional[Organization]


class RemotePortDetails(BaseResponse):
    Port: Optional[int]
    PortName: Optional[str]


class NetworkConnectionAction(BaseResponse):
    Blocked: Optional[bool]
    ConnectionDirection: Optional[str]
    LocalPortDetails: Optional[LocalPortDetails]
    Protocol: Optional[str]
    LocalIpDetails: Optional[LocalIpDetails]
    RemoteIpDetails: Optional[RemoteIpDetails1]
    RemotePortDetails: Optional[RemotePortDetails]


class RemoteIpDetails2(BaseResponse):
    City: Optional[City]
    Country: Optional[Country]
    GeoLocation: Optional[GeoLocation]
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]
    Organization: Optional[Organization]


class PortProbeDetail(BaseResponse):
    LocalPortDetails: Optional[LocalPortDetails]
    LocalIpDetails: Optional[LocalIpDetails]
    RemoteIpDetails: Optional[RemoteIpDetails2]


class PortProbeAction(BaseResponse):
    Blocked: Optional[bool]
    PortProbeDetails: Optional[List[PortProbeDetail]]


class RemoteIpDetails3(BaseResponse):
    City: Optional[City]
    Country: Optional[Country]
    GeoLocation: Optional[GeoLocation]
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]
    Organization: Optional[Organization]


class KubernetesApiCallAction(BaseResponse):
    RequestUri: Optional[str]
    Verb: Optional[str]
    SourceIps: Optional[List[str]]
    UserAgent: Optional[str]
    RemoteIpDetails: Optional[RemoteIpDetails3]
    StatusCode: Optional[int]
    Parameters: Optional[str]
    Resource: Optional[str]
    Subresource: Optional[str]
    Namespace: Optional[str]
    ResourceName: Optional[str]


class RemoteIpDetails4(BaseResponse):
    City: Optional[City]
    Country: Optional[Country]
    GeoLocation: Optional[GeoLocation]
    IpAddressV4: Optional[str]
    IpAddressV6: Optional[str]
    Organization: Optional[Organization]


class LoginAttribute(BaseResponse):
    User: Optional[str]
    Application: Optional[str]
    FailedLoginAttempts: Optional[int]
    SuccessfulLoginAttempts: Optional[int]


class RdsLoginAttemptAction(BaseResponse):
    RemoteIpDetails: Optional[RemoteIpDetails4]
    LoginAttributes: Optional[List[LoginAttribute]]


class KubernetesPermissionCheckedDetails(BaseResponse):
    Verb: Optional[str]
    Resource: Optional[str]
    Namespace: Optional[str]
    Allowed: Optional[bool]


class KubernetesRoleBindingDetails(BaseResponse):
    Kind: Optional[str]
    Name: Optional[str]
    Uid: Optional[str]
    RoleRefName: Optional[str]
    RoleRefKind: Optional[str]


class KubernetesRoleDetails(BaseResponse):
    Kind: Optional[str]
    Name: Optional[str]
    Uid: Optional[str]


class Action(BaseResponse):
    ActionType: Optional[str]
    AwsApiCallAction: Optional[AwsApiCallAction]
    DnsRequestAction: Optional[DnsRequestAction]
    NetworkConnectionAction: Optional[NetworkConnectionAction]
    PortProbeAction: Optional[PortProbeAction]
    KubernetesApiCallAction: Optional[KubernetesApiCallAction]
    RdsLoginAttemptAction: Optional[RdsLoginAttemptAction]
    KubernetesPermissionCheckedDetails: Optional[
        KubernetesPermissionCheckedDetails] = None
    KubernetesRoleBindingDetails: Optional[KubernetesRoleBindingDetails]
    KubernetesRoleDetails: Optional[KubernetesRoleDetails]


class ThreatIntelligenceDetail(BaseResponse):
    ThreatListName: Optional[str]
    ThreatNames: Optional[List[str]]
    ThreatFileSha256: Optional[str]


class Evidence(BaseResponse):
    ThreatIntelligenceDetails: Optional[List[ThreatIntelligenceDetail]]


class AdditionalInfo(BaseResponse):
    Value: Optional[str]
    Type: Optional[str]


class ScannedItemCount(BaseResponse):
    TotalGb: Optional[int]
    Files: Optional[int]
    Volumes: Optional[int]


class ThreatsDetectedItemCount(BaseResponse):
    Files: Optional[int]


class HighestSeverityThreatDetails(BaseResponse):
    Severity: Optional[str]
    ThreatName: Optional[str]
    Count: Optional[int]


class FilePath(BaseResponse):
    FilePath: Optional[str]
    VolumeArn: Optional[str]
    Hash: Optional[str]
    FileName: Optional[str]


class ThreatName(BaseResponse):
    Name: Optional[str]
    Severity: Optional[str]
    ItemCount: Optional[int]
    FilePaths: Optional[List[FilePath]]


class ThreatDetectedByName(BaseResponse):
    ItemCount: Optional[int]
    UniqueThreatNameCount: Optional[int]
    Shortened: Optional[bool]
    ThreatNames: Optional[List[ThreatName]]


class ScanDetections(BaseResponse):
    ScannedItemCount: Optional[ScannedItemCount]
    ThreatsDetectedItemCount: Optional[ThreatsDetectedItemCount]
    HighestSeverityThreatDetails: Optional[HighestSeverityThreatDetails]
    ThreatDetectedByName: Optional[ThreatDetectedByName]


class EbsVolumeScanDetails(BaseResponse):
    ScanId: Optional[str]
    ScanStartedAt: Optional[datetime]
    ScanCompletedAt: Optional[datetime]
    TriggerFindingId: Optional[str]
    Sources: Optional[List[str]]
    ScanDetections: Optional[ScanDetections]
    ScanType: Optional[ScanType]


class LineageItem(BaseResponse):
    StartTime: Optional[datetime]
    NamespacePid: Optional[int]
    UserId: Optional[int]
    Name: Optional[str]
    Pid: Optional[int]
    Uuid: Optional[str]
    ExecutablePath: Optional[str]
    Euid: Optional[int]
    ParentUuid: Optional[str]


class Process(BaseResponse):
    Name: Optional[str]
    ExecutablePath: Optional[str]
    ExecutableSha256: Optional[str]
    NamespacePid: Optional[int]
    Pwd: Optional[str]
    Pid: Optional[int]
    StartTime: Optional[datetime]
    Uuid: Optional[str]
    ParentUuid: Optional[str]
    User: Optional[str]
    UserId: Optional[int]
    Euid: Optional[int]
    Lineage: Optional[List[LineageItem]]


class ModifyingProcess(BaseResponse):
    Name: Optional[str]
    ExecutablePath: Optional[str]
    ExecutableSha256: Optional[str]
    NamespacePid: Optional[int]
    Pwd: Optional[str]
    Pid: Optional[int]
    StartTime: Optional[datetime]
    Uuid: Optional[str]
    ParentUuid: Optional[str]
    User: Optional[str]
    UserId: Optional[int]
    Euid: Optional[int]
    Lineage: Optional[List[LineageItem]]


class TargetProcess(BaseResponse):
    Name: Optional[str]
    ExecutablePath: Optional[str]
    ExecutableSha256: Optional[str]
    NamespacePid: Optional[int]
    Pwd: Optional[str]
    Pid: Optional[int]
    StartTime: Optional[datetime]
    Uuid: Optional[str]
    ParentUuid: Optional[str]
    User: Optional[str]
    UserId: Optional[int]
    Euid: Optional[int]
    Lineage: Optional[List[LineageItem]]


class Context(BaseResponse):
    ModifyingProcess: Optional[ModifyingProcess]
    ModifiedAt: Optional[datetime]
    ScriptPath: Optional[str]
    LibraryPath: Optional[str]
    LdPreloadValue: Optional[str]
    SocketPath: Optional[str]
    RuncBinaryPath: Optional[str]
    ReleaseAgentPath: Optional[str]
    MountSource: Optional[str]
    MountTarget: Optional[str]
    FileSystemType: Optional[str]
    Flags: Optional[List[str]]
    ModuleName: Optional[str]
    ModuleFilePath: Optional[str]
    ModuleSha256: Optional[str]
    ShellHistoryFilePath: Optional[str]
    TargetProcess: Optional[TargetProcess]
    AddressFamily: Optional[str]
    IanaProtocolNumber: Optional[int]
    MemoryRegions: Optional[List[str]]
    ToolName: Optional[str]
    ToolCategory: Optional[str]
    ServiceName: Optional[str]
    CommandLineExample: Optional[str]
    ThreatFilePath: Optional[str]


class RuntimeDetails(BaseResponse):
    Process: Optional[Process]
    Context: Optional[Context]


class Observations(BaseResponse):
    Text: Optional[List[str]]


class StringItem(BaseResponse):
    ProfileType: Optional[str]
    ProfileSubtype: Optional[ProfileSubtype]
    Observations: Optional[Observations]


class String(BaseResponse):
    string: Optional[List[StringItem]]


class Profiles(BaseResponse):
    string: Optional[String]


class String2(BaseResponse):
    ProfileType: Optional[str]
    ProfileSubtype: Optional[ProfileSubtype]
    Observations: Optional[Observations]


class String1(BaseResponse):
    string: Optional[String2]


class Behavior(BaseResponse):
    string: Optional[String1]


class Unusual(BaseResponse):
    Behavior: Optional[Behavior]


class Anomaly(BaseResponse):
    Profiles: Optional[Profiles]
    Unusual: Optional[Unusual]


class Detection(BaseResponse):
    Anomaly: Optional[Anomaly]


class ItemPath(BaseResponse):
    NestedItemPath: Optional[str]
    Hash: Optional[str]


class Threat(BaseResponse):
    Name: Optional[str]
    Source: Optional[str]
    ItemPaths: Optional[List[ItemPath]]


class MalwareScanDetails(BaseResponse):
    Threats: Optional[List[Threat]]


class Service(BaseResponse):
    Action: Optional[Action]
    Evidence: Optional[Evidence]
    Archived: Optional[bool]
    Count: Optional[int]
    DetectorId: Optional[str]
    EventFirstSeen: Optional[str]
    EventLastSeen: Optional[str]
    ResourceRole: Optional[str]
    ServiceName: Optional[str]
    UserFeedback: Optional[str]
    AdditionalInfo: Optional[AdditionalInfo]
    FeatureName: Optional[str]
    EbsVolumeScanDetails: Optional[EbsVolumeScanDetails]
    RuntimeDetails: Optional[RuntimeDetails]
    Detection: Optional[Detection]
    MalwareScanDetails: Optional[MalwareScanDetails]


class Finding(BaseResponse):
    AccountId: Optional[str]
    Arn: Optional[str]
    Confidence: Optional[float]
    CreatedAt: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Partition: Optional[str]
    Region: Optional[str]
    Resource: Optional[Resource]
    SchemaVersion: Optional[str]
    Service: Optional[Service]
    Severity: Optional[float]
    Title: Optional[str]
    Type: Optional[str]
    UpdatedAt: Optional[str]


class GetFindingsResponse(BaseResponse):
    Findings: Optional[List[Finding]]
