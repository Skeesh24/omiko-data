from typing import Union
from fastapi import APIRouter
from fastapi.params import Depends
from requests import codes

from app.classes.dependencies import get_uow
from app.classes.functions import try_get_repository
from app.models.repositories.repository_interface import IRepository
from app.models.validation import (
    CabinetRequestModel,
    OfficeRequestModel,
    OrderRequestModel,
    ProductCategoryRequestModel,
    ProductRequestModel,
    UserRequestModel,
)


put_router = APIRouter(prefix="/update", tags=["update"])


@put_router.put("/{tablename}", status_code=codes.created)
async def update_product(
    tablename: str,
    document_id: str,
    new_data: Union[
        ProductRequestModel,
        UserRequestModel,
        OrderRequestModel,
        ProductCategoryRequestModel,
        CabinetRequestModel,
        OfficeRequestModel,
    ],
    uow=Depends(get_uow),
) -> None:
    db: IRepository = try_get_repository(uow, tablename)
    db.update(document_id=document_id, element=new_data)
