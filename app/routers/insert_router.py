from typing import List, Union

from classes.dependencies import get_uow
from classes.functions import try_get_repository
from classes.interfaces import IRepository
from classes.validation import (
    CabinetRequestModel,
    CabinetResponseModel,
    OfficeRequestModel,
    OfficeResponseModel,
    OrderRequestModel,
    OrderResponseModel,
    ProductCategoryRequestModel,
    ProductCategoryResponseModel,
    ProductRequestModel,
    ProductResponseModel,
)
from fastapi import APIRouter, status
from fastapi.params import Depends

insert_router = APIRouter(prefix="/insert", tags=["insert"])


@insert_router.post(
    "/{tablename}",
    status_code=status.HTTP_201_CREATED,
    response_model=Union[
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
