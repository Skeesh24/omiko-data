from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database
from app.classes.dependencies import (
    get_cabinet_repository,
    get_office_repository,
    get_order_repository,
    get_product_category_repository,
    get_product_repository,
    get_user_repository,
)

from app.database.firebase import get_db
from app.models.repositories.repository_interface import IRepository
from app.models.validation import (
    CabinetRequestModel,
    CabinetResponseModel,
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


insert_router = APIRouter(prefix="/insert", tags=["insert"])


@insert_router.post(
    "/user", status_code=codes.created, response_model=UserResponseModel
)
async def insert(data: dict = Body(), db: IRepository = Depends(get_user_repository)):
    new_user: UserRequestModel = type_validation_check(UserRequestModel, data)

    response: UserResponseModel = type_validation_check(UserResponseModel, data)

    db.add(new_user)
    return response


@insert_router.post(
    "/product", status_code=codes.created, response_model=ProductResponseModel
)
async def insert(
    data: dict = Body(), db: IRepository = Depends(get_product_repository)
):
    new_product: ProductRequestModel = type_validation_check(ProductRequestModel, data)

    response: ProductResponseModel = type_validation_check(ProductResponseModel, data)

    db.add(new_product)
    return response


@insert_router.post(
    "/order", status_code=codes.created, response_model=OrderResponseModel
)
async def insert(data: dict = Body(), db: IRepository = Depends(get_order_repository)):
    new_order: OrderRequestModel = type_validation_check(OrderRequestModel, data)

    response: OrderResponseModel = type_validation_check(OrderResponseModel, data)

    db.add(new_order)
    return response


@insert_router.post(
    "/product_category",
    status_code=codes.created,
    response_model=ProductCategoryResponseModel,
)
async def insert(
    data: dict = Body(), db: IRepository = Depends(get_product_category_repository)
):
    new_category: ProductCategoryRequestModel = type_validation_check(
        ProductCategoryRequestModel, data
    )

    response: ProductCategoryResponseModel = type_validation_check(
        ProductCategoryResponseModel, data
    )

    db.add(new_category)
    return response


@insert_router.post(
    "/office",
    status_code=codes.created,
    response_model=OfficeResponseModel,
)
async def insert(data: dict = Body(), db: IRepository = Depends(get_office_repository)):
    new_office: OfficeRequestModel = type_validation_check(OfficeRequestModel, data)

    response: OfficeResponseModel = type_validation_check(OfficeResponseModel, data)

    db.add(new_office)
    return response


@insert_router.post(
    "/cabinet",
    status_code=codes.created,
    response_model=CabinetResponseModel,
)
async def insert(
    data: dict = Body(), db: IRepository = Depends(get_cabinet_repository)
):
    new_cabinet: CabinetRequestModel = type_validation_check(CabinetRequestModel, data)

    response: CabinetResponseModel = type_validation_check(CabinetResponseModel, data)

    db.add(new_cabinet)
    return response
