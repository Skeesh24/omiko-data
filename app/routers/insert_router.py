from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database
from fastapi.exceptions import HTTPException

from app.database.firebase import get_db
from app.models.validation import (
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
    new_user: UserResponseModel = type_validation_check(
        UserRequestModel, UserResponseModel, data
    )

    db.conn.collection("user").add(new_user.dict(exclude_defaults=True))
    return new_user


@insert_router.post(
    "/product", status_code=codes.created, response_model=ProductResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_product: ProductResponseModel = type_validation_check(
        ProductRequestModel, ProductResponseModel, data
    )

    db.conn.collection("product").add(new_product.dict(exclude_defaults=True))
    return new_product


@insert_router.post(
    "/order", status_code=codes.created, response_model=OrderResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_order: OrderResponseModel = type_validation_check(
        OrderRequestModel, OrderResponseModel, data
    )

    db.conn.collection("order").add(new_order.dict(exclude_defaults=True))
    return new_order
