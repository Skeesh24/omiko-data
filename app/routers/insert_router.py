from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database
from fastapi.exceptions import HTTPException

from app.database.firebase import get_db
from app.models.validation import (
    OfficeRequestModel,
    OfficeResponseModel,
    ProductCategoryRequestModel,
    ProductCategoryResponseModel,
    UserRequestModel,
    UserResponseModel,
    ProductRequestModel,
    ProductResponseModel,
    OrderRequestModel,
    OrderResponseModel,
)
from app.classes.functions import type_validation_check


insert_router = APIRouter(prefix="/insert", tags=["insert", "post"])


@insert_router.post(
    "/user", status_code=codes.created, response_model=UserResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_user: UserRequestModel = type_validation_check(UserRequestModel, data)

    response: UserResponseModel = type_validation_check(UserResponseModel, data)

    # replace this connection with a repository interface
    db.conn.collection("user").add(new_user.dict(exclude_defaults=True))
    return response


@insert_router.post(
    "/product", status_code=codes.created, response_model=ProductResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_product: ProductRequestModel = type_validation_check(ProductRequestModel, data)

    response: ProductResponseModel = type_validation_check(ProductResponseModel, data)

    # replace this connection with a repository interface
    db.conn.collection("product").add(new_product.dict(exclude_defaults=True))
    return response


@insert_router.post(
    "/order", status_code=codes.created, response_model=OrderResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_order: OrderRequestModel = type_validation_check(OrderRequestModel, data)

    response: OrderResponseModel = type_validation_check(OrderResponseModel, data)

    # replace this connection with a repository interface
    db.conn.collection("order").add(new_order.dict(exclude_defaults=True))
    return response


@insert_router.post(
    "/product_category",
    status_code=codes.created,
    response_model=ProductCategoryResponseModel,
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_category: ProductCategoryRequestModel = type_validation_check(
        ProductCategoryRequestModel, data
    )

    response: ProductCategoryResponseModel = type_validation_check(
        ProductCategoryResponseModel, data
    )

    # replace this connection with a repository interface
    db.conn.collection("product_category").add(new_category.dict(exclude_defaults=True))
    return response


@insert_router.post(
    "/office",
    status_code=codes.created,
    response_model=OfficeResponseModel,
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_office: OfficeRequestModel = type_validation_check(OfficeRequestModel, data)

    response: OfficeResponseModel = type_validation_check(OfficeResponseModel, data)

    # replace this connection with a repository interface
    db.conn.collection("office").add(new_office.dict(exclude_defaults=True))
    return response
