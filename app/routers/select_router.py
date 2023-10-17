from typing import List, Union

from classes.dependencies import get_uow
from classes.functions import is_list, try_get_repository
from classes.interfaces import IRepository
from classes.validation import (
    CabinetResponseModel,
    FilterRequestModel,
    OfficeResponseModel,
    OrderResponseModel,
    ProductCategoryResponseModel,
    ProductResponseModel,
)
from fastapi import APIRouter
from fastapi.params import Depends

select_router = APIRouter(prefix="/select", tags=["select"])


@select_router.post(
    "/{tablename}",
    response_model=Union[
        List[
            Union[
                ProductResponseModel,
                OrderResponseModel,
                ProductCategoryResponseModel,
                CabinetResponseModel,
                OfficeResponseModel,
            ]
        ],
        Union[
            ProductResponseModel,
            OrderResponseModel,
            ProductCategoryResponseModel,
            CabinetResponseModel,
            OfficeResponseModel,
        ],
    ],
)
async def select_users(
    tablename: str,
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    uow=Depends(get_uow),
):
    db: IRepository = try_get_repository(uow, tablename)

    elements = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return elements
