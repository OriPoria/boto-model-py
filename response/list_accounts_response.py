from __future__ import annotations
from enum import Enum
from datetime import datetime


class JoinedMethod(Enum):
    INVITED = 'INVITED'
    CREATED = 'CREATED'


class AccountsStatus(Enum):
    ACTIVE = 'ACTIVE'
    SUSPENDED = 'SUSPENDED'
    PENDING_CLOSURE = 'PENDING_CLOSURE'


from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class Account(BaseResponse):
    Id: Optional[str]
    Arn: Optional[str]
    Email: Optional[str]
    Name: Optional[str]
    Status: Optional[AccountsStatus]
    JoinedMethod: Optional[JoinedMethod]
    JoinedTimestamp: Optional[datetime]


class ListAccountsResponse(BaseResponse):
    Accounts: Optional[List[Account]]
    NextToken: Optional[str]
