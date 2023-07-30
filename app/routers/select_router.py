from typing import List
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
    get_cabinet_repository,
    get_office_repository,
    get_order_repository,
    get_product_category_repository,
    get_product_repository,
    get_user_repository,
)


select_router = APIRouter(prefix="/select", tags=["select"])


@select_router.post("/user", response_model=List[UserResponseModel])
async def select_users(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_user_repository),
) -> list[UserResponseModel]:
    users = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return [UserResponseModel(**u._data) for u in users] if len(users) > 0 else []


@select_router.post("/product", response_model=List[ProductResponseModel])
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


@select_router.post("/order", response_model=List[OrderResponseModel])
async def select_orders(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_order_repository),
) -> List[OrderResponseModel]:
    orders = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return [OrderResponseModel(**o._data) for o in orders] if len(orders) > 0 else []


@select_router.post(
    "/product_category", response_model=List[ProductCategoryResponseModel]
)
async def select_product_categories(
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


@select_router.post("/office", response_model=List[OfficeResponseModel])
async def select_offices(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_office_repository),
) -> List[OfficeResponseModel]:
    offices = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return (
        [OfficeResponseModel(**of.to_dict()) for of in offices]
        if len(offices) > 0
        else []
    )


@select_router.post("/cabinet", response_model=List[CabinetResponseModel])
async def select_cabinets(
    limit: int = 5,
    offset: int = 0,
    document_id: str = "",
    where: FilterRequestModel = None,
    db: IRepository = Depends(get_cabinet_repository),
) -> List[CabinetResponseModel]:
    cabinets = db.get(limit=limit, offset=offset, document_id=document_id, where=where)

    return (
        [CabinetResponseModel(**cab.to_dict()) for cab in cabinets]
        if len(cabinets) > 0
        else []
    )
