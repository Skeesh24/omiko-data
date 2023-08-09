from typing import List, Union
from fastapi import APIRouter
from fastapi.params import Depends
from requests.status_codes import codes
from app.classes.dependencies import get_uow
from app.classes.functions import try_get_repository

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


insert_router = APIRouter(prefix="/insert", tags=["insert"])


@insert_router.post(
    "/{tablename}",
    status_code=codes.created,
    response_model=Union[
        UserResponseModel,
        ProductResponseModel,
        OrderResponseModel,
        ProductCategoryResponseModel,
        CabinetResponseModel,
        OfficeResponseModel,
    ],
)
async def insert(
    tablename: str,
    data: Union[
        UserRequestModel,
        ProductRequestModel,
        OrderRequestModel,
        ProductCategoryRequestModel,
        OfficeRequestModel,
        CabinetRequestModel,
    ],
    uow=Depends(get_uow),
):
    db: IRepository = try_get_repository(uow, tablename)
    db.add(data)
    return data
