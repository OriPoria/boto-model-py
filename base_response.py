from pydantic import BaseModel
from typing import Dict, Any


class BaseResponse(BaseModel):
    def __init__(self, **data: Dict[str, Any]):
        # Extract the fields defined in the model
        fields = self.__fields__.keys()

        # Initialize the dictionary with None for missing fields
        init_data = {field: data.get(field, None) for field in fields}

        # Call the parent __init__ method with the initialized data
        super().__init__(**init_data)
