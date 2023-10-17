from typing import Any, List

from pydantic import BaseModel


class FilterRequestModel(BaseModel):
    field_path: str
    op_string: str
    value: Any


class ProductRequestModel(BaseModel):
    name: str
    description: str
    short_description: str
    price: float
    category: str


class ProductResponseModel(BaseModel):
    id: str
    name: str
    price: float
    category: str


class OrderRequestModel(BaseModel):
    user: str
    products: List[str]
    price: float


class OrderResponseModel(BaseModel):
    id: str
    user: str
    products: List[str]
    price: float


class ProductCategoryRequestModel(BaseModel):
    name: str
    product_count: int


class ProductCategoryResponseModel(BaseModel):
    id: str
    name: str
    product_count: int


class OfficeRequestModel(BaseModel):
    city: str
    address: str
    phone: str
    email: str


class OfficeResponseModel(BaseModel):
    id: str
    city: str
    address: str
    phone: str
    email: str


class CabinetRequestModel(BaseModel):
    cart: List[str]
    favourites: List[str]
    orders: List[str]
    city: str
    phone: str


class CabinetResponseModel(BaseModel):
    id: str
    cart: List[str]
    favourites: List[str]
    orders: List[str]
    city: str
    phone: str
