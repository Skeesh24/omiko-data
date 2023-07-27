from typing import List
from fastapi import APIRouter
from app.database.entities import Product, User
from app.models.repositories.repository import FirebaseRepository

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
async def select(
    limit: int = 5,
    offset: int = 0,
    where: FilterRequestModel = None,
    db: FirebaseRepository[User] = Depends(get_user_repository),
) -> list[UserResponseModel]:
    all = db.get_all()

    return [UserResponseModel(**x.to_dict()) for x in all]


@select_router.get("/product", response_model=ProductResponseModel)
async def select_product(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: FirebaseRepository[Product] = Depends(get_product_repository),
) -> ProductResponseModel:
    element = db.get(document_id=document_id)

    return element
