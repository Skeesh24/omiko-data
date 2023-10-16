from typing import Union

from classes.dependencies import get_uow
from classes.functions import try_get_repository
from classes.interfaces import IRepository
from classes.validation import (
    CabinetRequestModel,
    OfficeRequestModel,
    OrderRequestModel,
    ProductCategoryRequestModel,
    ProductRequestModel,
)
from fastapi import APIRouter, status
from fastapi.params import Depends

put_router = APIRouter(prefix="/update", tags=["update"])


@put_router.put("/{tablename}", status_code=status.HTTP_201_CREATED)
async def update_product(
    tablename: str,
    id: str,
    new_data: Union[
        ProductRequestModel,
        OrderRequestModel,
        ProductCategoryRequestModel,
        CabinetRequestModel,
        OfficeRequestModel,
    ],
    uow=Depends(get_uow),
) -> None:
    db: IRepository = try_get_repository(uow, tablename)
    db.update(id=id, update_elem=new_data)
