from __future__ import annotations
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class SystemLogLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'


class ApplicationLogLevel(Enum):
    TRACE = 'TRACE'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    FATAL = 'FATAL'


class LogFormat(Enum):
    JSON = 'JSON'
    TEXT = 'Text'


class OptimizationStatus(Enum):
    ON = 'On'
    OFF = 'Off'


class ApplyOn(Enum):
    PUBLISHED_VERSIONS = 'PublishedVersions'
    NONE = 'None'


class Architectures(Enum):
    X86_64 = 'x86_64'
    ARM64 = 'arm64'


class PackageType(Enum):
    ZIP = 'Zip'
    IMAGE = 'Image'


class LastUpdateStatusReasonCode(Enum):
    ENI_LIMIT_EXCEEDED = 'EniLimitExceeded'
    INSUFFICIENT_ROLE_PERMISSIONS = 'InsufficientRolePermissions'
    INVALID_CONFIGURATION = 'InvalidConfiguration'
    INTERNAL_ERROR = 'InternalError'
    SUBNET_OUT_OF_I_P_ADDRESSES = 'SubnetOutOfIPAddresses'
    INVALID_SUBNET = 'InvalidSubnet'
    INVALID_SECURITY_GROUP = 'InvalidSecurityGroup'
    IMAGE_DELETED = 'ImageDeleted'
    IMAGE_ACCESS_DENIED = 'ImageAccessDenied'
    INVALID_IMAGE = 'InvalidImage'
    K_M_S_KEY_ACCESS_DENIED = 'KMSKeyAccessDenied'
    K_M_S_KEY_NOT_FOUND = 'KMSKeyNotFound'
    INVALID_STATE_K_M_S_KEY = 'InvalidStateKMSKey'
    DISABLED_K_M_S_KEY = 'DisabledKMSKey'
    E_F_S_I_O_ERROR = 'EFSIOError'
    E_F_S_MOUNT_CONNECTIVITY_ERROR = 'EFSMountConnectivityError'
    E_F_S_MOUNT_FAILURE = 'EFSMountFailure'
    E_F_S_MOUNT_TIMEOUT = 'EFSMountTimeout'
    INVALID_RUNTIME = 'InvalidRuntime'
    INVALID_ZIP_FILE_EXCEPTION = 'InvalidZipFileException'
    FUNCTION_ERROR = 'FunctionError'


class LastUpdateStatus(Enum):
    SUCCESSFUL = 'Successful'
    FAILED = 'Failed'
    IN_PROGRESS = 'InProgress'


class StateReasonCode(Enum):
    IDLE = 'Idle'
    CREATING = 'Creating'
    RESTORING = 'Restoring'
    ENI_LIMIT_EXCEEDED = 'EniLimitExceeded'
    INSUFFICIENT_ROLE_PERMISSIONS = 'InsufficientRolePermissions'
    INVALID_CONFIGURATION = 'InvalidConfiguration'
    INTERNAL_ERROR = 'InternalError'
    SUBNET_OUT_OF_I_P_ADDRESSES = 'SubnetOutOfIPAddresses'
    INVALID_SUBNET = 'InvalidSubnet'
    INVALID_SECURITY_GROUP = 'InvalidSecurityGroup'
    IMAGE_DELETED = 'ImageDeleted'
    IMAGE_ACCESS_DENIED = 'ImageAccessDenied'
    INVALID_IMAGE = 'InvalidImage'
    K_M_S_KEY_ACCESS_DENIED = 'KMSKeyAccessDenied'
    K_M_S_KEY_NOT_FOUND = 'KMSKeyNotFound'
    INVALID_STATE_K_M_S_KEY = 'InvalidStateKMSKey'
    DISABLED_K_M_S_KEY = 'DisabledKMSKey'
    E_F_S_I_O_ERROR = 'EFSIOError'
    E_F_S_MOUNT_CONNECTIVITY_ERROR = 'EFSMountConnectivityError'
    E_F_S_MOUNT_FAILURE = 'EFSMountFailure'
    E_F_S_MOUNT_TIMEOUT = 'EFSMountTimeout'
    INVALID_RUNTIME = 'InvalidRuntime'
    INVALID_ZIP_FILE_EXCEPTION = 'InvalidZipFileException'
    FUNCTION_ERROR = 'FunctionError'


class FunctionsState(Enum):
    PENDING = 'Pending'
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    FAILED = 'Failed'


class Mode(Enum):
    ACTIVE = 'Active'
    PASS_THROUGH = 'PassThrough'


class Runtime(Enum):
    NODEJS = 'nodejs'
    NODEJS43 = 'nodejs4.3'
    NODEJS610 = 'nodejs6.10'
    NODEJS810 = 'nodejs8.10'
    NODEJS10X = 'nodejs10.x'
    NODEJS12X = 'nodejs12.x'
    NODEJS14X = 'nodejs14.x'
    NODEJS16X = 'nodejs16.x'
    JAVA8 = 'java8'
    JAVA8AL2 = 'java8.al2'
    JAVA11 = 'java11'
    PYTHON27 = 'python2.7'
    PYTHON36 = 'python3.6'
    PYTHON37 = 'python3.7'
    PYTHON38 = 'python3.8'
    PYTHON39 = 'python3.9'
    DOTNETCORE10 = 'dotnetcore1.0'
    DOTNETCORE20 = 'dotnetcore2.0'
    DOTNETCORE21 = 'dotnetcore2.1'
    DOTNETCORE31 = 'dotnetcore3.1'
    DOTNET6 = 'dotnet6'
    DOTNET8 = 'dotnet8'
    NODEJS43EDGE = 'nodejs4.3-edge'
    GO1X = 'go1.x'
    RUBY25 = 'ruby2.5'
    RUBY27 = 'ruby2.7'
    PROVIDED = 'provided'
    PROVIDEDAL2 = 'provided.al2'
    NODEJS18X = 'nodejs18.x'
    PYTHON310 = 'python3.10'
    JAVA17 = 'java17'
    RUBY32 = 'ruby3.2'
    RUBY33 = 'ruby3.3'
    PYTHON311 = 'python3.11'
    NODEJS20X = 'nodejs20.x'
    PROVIDEDAL2023 = 'provided.al2023'
    PYTHON312 = 'python3.12'
    JAVA21 = 'java21'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class VpcConfig(BaseResponse):
    SubnetIds: Optional[List[str]]
    SecurityGroupIds: Optional[List[str]]
    VpcId: Optional[str]
    Ipv6AllowedForDualStack: Optional[bool]


class DeadLetterConfig(BaseResponse):
    TargetArn: Optional[str]


class Variables(BaseResponse):
    string: Optional[str]


class Error(BaseResponse):
    ErrorCode: Optional[str]
    Message: Optional[str]


class Environment(BaseResponse):
    Variables: Optional[Variables]
    Error: Optional[Error]


class TracingConfig(BaseResponse):
    Mode: Optional[Mode]


class Layer(BaseResponse):
    Arn: Optional[str]
    CodeSize: Optional[int]
    SigningProfileVersionArn: Optional[str]
    SigningJobArn: Optional[str]


class FileSystemConfig(BaseResponse):
    Arn: Optional[str]
    LocalMountPath: Optional[str]


class ImageConfig(BaseResponse):
    EntryPoint: Optional[List[str]]
    Command: Optional[List[str]]
    WorkingDirectory: Optional[str]


class ImageConfigResponse(BaseResponse):
    ImageConfig: Optional[ImageConfig]
    Error: Optional[Error]


class EphemeralStorage(BaseResponse):
    Size: Optional[int]


class SnapStart(BaseResponse):
    ApplyOn: Optional[ApplyOn]
    OptimizationStatus: Optional[OptimizationStatus]


class RuntimeVersionConfig(BaseResponse):
    RuntimeVersionArn: Optional[str]
    Error: Optional[Error]


class LoggingConfig(BaseResponse):
    LogFormat: Optional[LogFormat]
    ApplicationLogLevel: Optional[ApplicationLogLevel]
    SystemLogLevel: Optional[SystemLogLevel]
    LogGroup: Optional[str]


class Function(BaseResponse):
    FunctionName: Optional[str]
    FunctionArn: Optional[str]
    Runtime: Optional[Runtime]
    Role: Optional[str]
    Handler: Optional[str]
    CodeSize: Optional[int]
    Description: Optional[str]
    Timeout: Optional[int]
    MemorySize: Optional[int]
    LastModified: Optional[str]
    CodeSha256: Optional[str]
    Version: Optional[str]
    VpcConfig: Optional[VpcConfig]
    DeadLetterConfig: Optional[DeadLetterConfig]
    Environment: Optional[Environment]
    KMSKeyArn: Optional[str]
    TracingConfig: Optional[TracingConfig]
    MasterArn: Optional[str]
    RevisionId: Optional[str]
    Layers: Optional[List[Layer]]
    State: Optional[FunctionsState]
    StateReason: Optional[str]
    StateReasonCode: Optional[StateReasonCode]
    LastUpdateStatus: Optional[LastUpdateStatus]
    LastUpdateStatusReason: Optional[str]
    LastUpdateStatusReasonCode: Optional[LastUpdateStatusReasonCode]
    FileSystemConfigs: Optional[List[FileSystemConfig]]
    PackageType: Optional[PackageType]
    ImageConfigResponse: Optional[ImageConfigResponse]
    SigningProfileVersionArn: Optional[str]
    SigningJobArn: Optional[str]
    Architectures: Optional[List[Architectures]]
    EphemeralStorage: Optional[EphemeralStorage]
    SnapStart: Optional[SnapStart]
    RuntimeVersionConfig: Optional[RuntimeVersionConfig]
    LoggingConfig: Optional[LoggingConfig]


class ListFunctionsResponse(BaseResponse):
    NextMarker: Optional[str]
    Functions: Optional[List[Function]]
