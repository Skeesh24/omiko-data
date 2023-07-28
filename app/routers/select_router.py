from typing import List
from fastapi import APIRouter
from app.database.entities import Product, User
from app.models.repositories.repository import FirebaseRepository
from app.models.repositories.repository_interface import IRepository

from app.models.validation import (
    FilterRequestModel,
    OrderResponseModel,
    ProductCategoryResponseModel,
    ProductResponseModel,
    UserResponseModel,
)
from fastapi.params import Depends

from app.classes.dependencies import (
    get_order_repository,
    get_product_category_repository,
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

    return [ProductResponseModel(**u._data) for u in users] if len(users) > 0 else []


@select_router.get("/product", response_model=List[ProductResponseModel])
async def select_products(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_product_repository),
) -> List[ProductResponseModel]:
    products = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return (
        [ProductResponseModel(**p._data) for p in products] if len(products) > 0 else []
    )


@select_router.get("/order", response_model=List[OrderResponseModel])
async def select_products(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_order_repository),
) -> List[OrderResponseModel]:
    orders = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return [OrderResponseModel(**o._data) for o in orders] if len(orders) > 0 else []


@select_router.get(
    "/product_category", response_model=List[ProductCategoryResponseModel]
)
async def select_products(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_product_category_repository),
) -> List[ProductCategoryResponseModel]:
    categories = db.get(
        limit=limit, offset=offset, document_id=document_id, where=where
    )

    return (
        [ProductCategoryResponseModel(**pc._data) for pc in categories]
        if len(categories) > 0
        else []
    )
