from typing import List, Union
from fastapi import APIRouter
from app.models.repositories.repository_interface import IRepository

from app.models.validation import (
    CabinetResponseModel,
    FilterRequestModel,
    OfficeResponseModel,
    OrderResponseModel,
    ProductCategoryResponseModel,
    ProductResponseModel,
    UserResponseModel,
    FilterRequestModel,
)
from fastapi.params import Depends

from app.classes.dependencies import (
    get_uow,
)


select_router = APIRouter(prefix="/select", tags=["select"])


@select_router.post(
    "/{tablename}",
    response_model=List[
        Union[
            UserResponseModel,
            ProductResponseModel,
            OrderResponseModel,
            ProductCategoryResponseModel,
            CabinetResponseModel,
            OfficeResponseModel,
        ]
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
    db: IRepository = uow.__getattribute__(tablename)

    elements = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return [e._data for e in elements] if len(elements) > 0 else []
