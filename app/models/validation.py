from pydantic import BaseModel, Field
from typing import Any


class FilterRequestModel(BaseModel):
    field_path: str
    op_string: str
    value: Any


class UserRequestModel(BaseModel):
    email: str
    password: str


class UserResponseModel(BaseModel):
    email: str


class ProductRequestModel(BaseModel):
    name: str
    description: str
    short_description: str
    price: float
    category: str


class ProductResponseModel(BaseModel):
    name: str
    price: float
    category: str


class OrderRequestModel(BaseModel):
    pass


class OrderResponseModel(BaseModel):
    pass
