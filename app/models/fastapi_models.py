from pydantic import BaseModel, Field
from typing import Any


class firebase_filter(BaseModel):
    field_path: str 
    op_string: str 
    value: Any 
