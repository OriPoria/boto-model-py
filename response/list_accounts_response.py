from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class JoinedMethod(Enum):
    INVITED = 'INVITED'
    CREATED = 'CREATED'


class AccountsStatus(Enum):
    ACTIVE = 'ACTIVE'
    SUSPENDED = 'SUSPENDED'
    PENDING_CLOSURE = 'PENDING_CLOSURE'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


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
