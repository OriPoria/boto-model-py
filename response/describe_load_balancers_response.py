from __future__ import annotations
from enum import Enum
from datetime import datetime


class IpAddressType(Enum):
    IPV4 = 'ipv4'
    DUALSTACK = 'dualstack'
    DUALSTACKWITHOUTPUBLICIPV4 = 'dualstack-without-public-ipv4'


class Type(Enum):
    APPLICATION = 'application'
    NETWORK = 'network'
    GATEWAY = 'gateway'


class Code(Enum):
    ACTIVE = 'active'
    PROVISIONING = 'provisioning'
    ACTIVE_IMPAIRED = 'active_impaired'
    FAILED = 'failed'


class Scheme(Enum):
    INTERNETFACING = 'internet-facing'
    INTERNAL = 'internal'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class State(BaseResponse):
    Code: Optional[Code]
    Reason: Optional[str]


class LoadBalancerAddress(BaseResponse):
    IpAddress: Optional[str]
    AllocationId: Optional[str]
    PrivateIPv4Address: Optional[str]
    IPv6Address: Optional[str]


class AvailabilityZone(BaseResponse):
    ZoneName: Optional[str]
    SubnetId: Optional[str]
    OutpostId: Optional[str]
    LoadBalancerAddresses: Optional[List[LoadBalancerAddress]]


class LoadBalancer(BaseResponse):
    LoadBalancerArn: Optional[str]
    DNSName: Optional[str]
    CanonicalHostedZoneId: Optional[str]
    CreatedTime: Optional[datetime]
    LoadBalancerName: Optional[str]
    Scheme: Optional[Scheme]
    VpcId: Optional[str]
    State: Optional[State]
    Type: Optional[Type]
    AvailabilityZones: Optional[List[AvailabilityZone]]
    SecurityGroups: Optional[List[str]]
    IpAddressType: Optional[IpAddressType]
    CustomerOwnedIpv4Pool: Optional[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Optional[str]


class DescribeLoadBalancersResponse(BaseResponse):
    LoadBalancers: Optional[List[LoadBalancer]]
    NextMarker: Optional[str]
