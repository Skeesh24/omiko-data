from pydantic import BaseModel, Field
from typing import Any, List


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
    user: str
    products: List[str]
    price: float


class OrderResponseModel(BaseModel):
    user: str
    products: List[str]
    price: float


class ProductCategoryRequestModel(BaseModel):
    name: str
    product_count: int


class ProductCategoryResponseModel(BaseModel):
    name: str
    product_count: int


class OfficeRequestModel(BaseModel):
    city: str
    address: str
    phone: str
    email: str


class OfficeResponseModel(BaseModel):
    city: str
    address: str
    phone: str
    email: str
