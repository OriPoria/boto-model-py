from __future__ import annotations
from enum import Enum
from datetime import datetime


class MacAlgorithms(Enum):
    HMAC_SHA_224 = 'HMAC_SHA_224'
    HMAC_SHA_256 = 'HMAC_SHA_256'
    HMAC_SHA_384 = 'HMAC_SHA_384'
    HMAC_SHA_512 = 'HMAC_SHA_512'


class MultiRegionKeyType(Enum):
    PRIMARY = 'PRIMARY'
    REPLICA = 'REPLICA'


class SigningAlgorithms(Enum):
    RSASSA_PSS_SHA_256 = 'RSASSA_PSS_SHA_256'
    RSASSA_PSS_SHA_384 = 'RSASSA_PSS_SHA_384'
    RSASSA_PSS_SHA_512 = 'RSASSA_PSS_SHA_512'
    RSASSA_PKCS1_V1_5_SHA_256 = 'RSASSA_PKCS1_V1_5_SHA_256'
    RSASSA_PKCS1_V1_5_SHA_384 = 'RSASSA_PKCS1_V1_5_SHA_384'
    RSASSA_PKCS1_V1_5_SHA_512 = 'RSASSA_PKCS1_V1_5_SHA_512'
    ECDSA_SHA_256 = 'ECDSA_SHA_256'
    ECDSA_SHA_384 = 'ECDSA_SHA_384'
    ECDSA_SHA_512 = 'ECDSA_SHA_512'
    SM2DSA = 'SM2DSA'


class EncryptionAlgorithms(Enum):
    SYMMETRIC_DEFAULT = 'SYMMETRIC_DEFAULT'
    RSAES_OAEP_SHA_1 = 'RSAES_OAEP_SHA_1'
    RSAES_OAEP_SHA_256 = 'RSAES_OAEP_SHA_256'
    SM2PKE = 'SM2PKE'


class KeySpec(Enum):
    RSA_2048 = 'RSA_2048'
    RSA_3072 = 'RSA_3072'
    RSA_4096 = 'RSA_4096'
    ECC_NIST_P256 = 'ECC_NIST_P256'
    ECC_NIST_P384 = 'ECC_NIST_P384'
    ECC_NIST_P521 = 'ECC_NIST_P521'
    ECC_SECG_P256K1 = 'ECC_SECG_P256K1'
    SYMMETRIC_DEFAULT = 'SYMMETRIC_DEFAULT'
    HMAC_224 = 'HMAC_224'
    HMAC_256 = 'HMAC_256'
    HMAC_384 = 'HMAC_384'
    HMAC_512 = 'HMAC_512'
    SM2 = 'SM2'


class CustomerMasterKeySpec(Enum):
    RSA_2048 = 'RSA_2048'
    RSA_3072 = 'RSA_3072'
    RSA_4096 = 'RSA_4096'
    ECC_NIST_P256 = 'ECC_NIST_P256'
    ECC_NIST_P384 = 'ECC_NIST_P384'
    ECC_NIST_P521 = 'ECC_NIST_P521'
    ECC_SECG_P256K1 = 'ECC_SECG_P256K1'
    SYMMETRIC_DEFAULT = 'SYMMETRIC_DEFAULT'
    HMAC_224 = 'HMAC_224'
    HMAC_256 = 'HMAC_256'
    HMAC_384 = 'HMAC_384'
    HMAC_512 = 'HMAC_512'
    SM2 = 'SM2'


class KeyManager(Enum):
    AWS = 'AWS'
    CUSTOMER = 'CUSTOMER'


class ExpirationModel(Enum):
    KEY_MATERIAL_EXPIRES = 'KEY_MATERIAL_EXPIRES'
    KEY_MATERIAL_DOES_NOT_EXPIRE = 'KEY_MATERIAL_DOES_NOT_EXPIRE'


class Origin(Enum):
    AWS_KMS = 'AWS_KMS'
    EXTERNAL = 'EXTERNAL'
    AWS_CLOUDHSM = 'AWS_CLOUDHSM'
    EXTERNAL_KEY_STORE = 'EXTERNAL_KEY_STORE'


class KeyState(Enum):
    CREATING = 'Creating'
    ENABLED = 'Enabled'
    DISABLED = 'Disabled'
    PENDING_DELETION = 'PendingDeletion'
    PENDING_IMPORT = 'PendingImport'
    PENDING_REPLICA_DELETION = 'PendingReplicaDeletion'
    UNAVAILABLE = 'Unavailable'
    UPDATING = 'Updating'


class KeyUsage(Enum):
    SIGN_VERIFY = 'SIGN_VERIFY'
    ENCRYPT_DECRYPT = 'ENCRYPT_DECRYPT'
    GENERATE_VERIFY_MAC = 'GENERATE_VERIFY_MAC'
    KEY_AGREEMENT = 'KEY_AGREEMENT'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class PrimaryKey(BaseResponse):
    Arn: Optional[str]
    Region: Optional[str]


class ReplicaKey(BaseResponse):
    Arn: Optional[str]
    Region: Optional[str]


class MultiRegionConfiguration(BaseResponse):
    MultiRegionKeyType: Optional[MultiRegionKeyType]
    PrimaryKey: Optional[PrimaryKey]
    ReplicaKeys: Optional[List[ReplicaKey]]


class XksKeyConfiguration(BaseResponse):
    Id: Optional[str]


class KeyMetadata(BaseResponse):
    AWSAccountId: Optional[str]
    KeyId: Optional[str]
    Arn: Optional[str]
    CreationDate: Optional[datetime]
    Enabled: Optional[bool]
    Description: Optional[str]
    KeyUsage: Optional[KeyUsage]
    KeyState: Optional[KeyState]
    DeletionDate: Optional[datetime]
    ValidTo: Optional[datetime]
    Origin: Optional[Origin]
    CustomKeyStoreId: Optional[str]
    CloudHsmClusterId: Optional[str]
    ExpirationModel: Optional[ExpirationModel]
    KeyManager: Optional[KeyManager]
    CustomerMasterKeySpec: Optional[CustomerMasterKeySpec]
    KeySpec: Optional[KeySpec]
    EncryptionAlgorithms: Optional[List[EncryptionAlgorithms]]
    SigningAlgorithms: Optional[List[SigningAlgorithms]]
    KeyAgreementAlgorithms: Optional[List[str]]
    MultiRegion: Optional[bool]
    MultiRegionConfiguration: Optional[MultiRegionConfiguration]
    PendingDeletionWindowInDays: Optional[int]
    MacAlgorithms: Optional[List[MacAlgorithms]]
    XksKeyConfiguration: Optional[XksKeyConfiguration]


class DescribeKeyResponse(BaseResponse):
    KeyMetadata: Optional[KeyMetadata]
