from typing import List
from fastapi import APIRouter
from app.database.entities import Product, User
from app.models.repositories.repository import FirebaseRepository
from app.models.repositories.repository_interface import IRepository

from app.models.validation import (
    FilterRequestModel,
    ProductResponseModel,
    UserResponseModel,
)
from fastapi.params import Depends

from app.classes.dependencies import (
    get_product_repository,
    get_user_repository,
)
from app.models.validation import FilterRequestModel


select_router = APIRouter(prefix="/select", tags=["select"])


@select_router.get("/user", response_model=List[UserResponseModel])
async def select_users(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_user_repository),
) -> list[UserResponseModel]:
    users = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return [UserResponseModel(**x.to_dict()) for x in users]


@select_router.get("/product", response_model=ProductResponseModel)
async def select_products(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_product_repository),
) -> ProductResponseModel:
    products = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return products
