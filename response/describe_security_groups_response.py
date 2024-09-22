from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class IpRange(BaseResponse):
    CidrIp: Optional[str]
    Description: Optional[str]


class Ipv6Range(BaseResponse):
    CidrIpv6: Optional[str]
    Description: Optional[str]


class PrefixListId(BaseResponse):
    Description: Optional[str]
    PrefixListId: Optional[str]


class UserIdGroupPair(BaseResponse):
    Description: Optional[str]
    GroupId: Optional[str]
    GroupName: Optional[str]
    PeeringStatus: Optional[str]
    UserId: Optional[str]
    VpcId: Optional[str]
    VpcPeeringConnectionId: Optional[str]


class IpPermission(BaseResponse):
    FromPort: Optional[int]
    IpProtocol: Optional[str]
    IpRanges: Optional[List[IpRange]]
    Ipv6Ranges: Optional[List[Ipv6Range]]
    PrefixListIds: Optional[List[PrefixListId]]
    ToPort: Optional[int]
    UserIdGroupPairs: Optional[List[UserIdGroupPair]]


class IpPermissionsEgres(BaseResponse):
    FromPort: Optional[int]
    IpProtocol: Optional[str]
    IpRanges: Optional[List[IpRange]]
    Ipv6Ranges: Optional[List[Ipv6Range]]
    PrefixListIds: Optional[List[PrefixListId]]
    ToPort: Optional[int]
    UserIdGroupPairs: Optional[List[UserIdGroupPair]]


class Tag(BaseResponse):
    Key: Optional[str]
    Value: Optional[str]


class SecurityGroup(BaseResponse):
    Description: Optional[str]
    GroupName: Optional[str]
    IpPermissions: Optional[List[IpPermission]]
    OwnerId: Optional[str]
    GroupId: Optional[str]
    IpPermissionsEgress: Optional[List[IpPermissionsEgres]]
    Tags: Optional[List[Tag]]
    VpcId: Optional[str]


class DescribeSecurityGroupsResponse(BaseResponse):
    SecurityGroups: Optional[List[SecurityGroup]]
    NextToken: Optional[str]
