from pydantic import BaseModel, Field
from typing import Any, List


class FilterRequestModel(BaseModel):
    field_path: str
    op_string: str
    value: Any


class ProductRequestModel(BaseModel):
    email: str
    password: str


class ProductResponseModel(BaseModel):
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
    user: str
    products: List[float]
    price: float


class OrderResponseModel(BaseModel):
    user: str
    product: List[str]
    price: float
