from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database
from fastapi.exceptions import HTTPException

from app.database.firebase import get_db
from app.models.validation import (
    OrderRequestModel,
    OrderResponseModel,
    ProductRequestModel,
    ProductResponseModel,
    UserRequestModel,
    UserResponseModel,
)
from app.classes.functions import type_validation_check


insert_router = APIRouter(prefix="/insert", tags=["insert", "post"])


@insert_router.post(
    "/user", status_code=codes.created, response_model=UserResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    new_user: UserRequestModel = type_validation_check(UserRequestModel, data)

    db.conn.collection("user").add(data)
    return UserResponseModel(**data)


@insert_router.post(
    "/product", status_code=codes.created, response_model=ProductResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    try:
        ProductRequestModel(**data)
    except Exception as e:  # TODO clear e
        raise HTTPException(status_code=codes.bad_request, detail=str(e))
    db.conn.collection("product").add(data)
    return ProductResponseModel(**data)


@insert_router.post(
    "/order", status_code=codes.created, response_model=OrderResponseModel
)
async def insert(data: dict = Body(), db: Database = Depends(get_db)):
    try:
        OrderRequestModel(**data)
    except Exception as e:  # TODO clear e
        raise HTTPException(status_code=codes.bad_request, detail=str(e))
    db.conn.collection("order").add(data)
    return OrderResponseModel(**data)
