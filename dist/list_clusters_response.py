from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.__fields__.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


from typing import List, Optional
from pydantic import BaseModel


class ListClustersResponse(BaseResponse):
    clusters: Optional[List[str]]
    nextToken: Optional[str]
