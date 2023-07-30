from fastapi import APIRouter
from fastapi.params import Depends
from requests import codes

from app.classes.dependencies import (
    get_cabinet_repository,
    get_order_repository,
    get_product_category_repository,
    get_product_repository,
    get_user_repository,
)
from app.models.repositories.repository_interface import IRepository
from app.models.validation import (
    ProductResponseModel,
    ProductRequestModel,
    UserRequestModel,
    UserResponseModel,
    ProductCategoryRequestModel,
    ProductCategoryResponseModel,
    OfficeRequestModel,
    OfficeResponseModel,
    OrderRequestModel,
    OrderResponseModel,
    CabinetRequestModel,
    CabinetResponseModel,
)


put_router = APIRouter(prefix="update", tags=["update"])


@put_router.put("/user", response_model=UserResponseModel, status_code=codes.created)
async def update_product(
    document_id: str,
    new_product: UserRequestModel,
    db: IRepository = Depends(get_user_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)


@put_router.put(
    "/product", response_model=ProductResponseModel, status_code=codes.created
)
async def update_product(
    document_id: str,
    new_product: ProductRequestModel,
    db: IRepository = Depends(get_product_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)


@put_router.put("/order", response_model=OrderResponseModel, status_code=codes.created)
async def update_product(
    document_id: str,
    new_product: OrderRequestModel,
    db: IRepository = Depends(get_order_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)


@put_router.put(
    "/product_category",
    response_model=ProductCategoryResponseModel,
    status_code=codes.created,
)
async def update_product(
    document_id: str,
    new_product: ProductCategoryRequestModel,
    db: IRepository = Depends(get_product_category_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)


@put_router.put(
    "/office",
    response_model=OfficeResponseModel,
    status_code=codes.created,
)
async def update_product(
    document_id: str,
    new_product: OfficeRequestModel,
    db: IRepository = Depends(get_product_category_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)


@put_router.put(
    "/cabinet",
    response_model=CabinetResponseModel,
    status_code=codes.created,
)
async def update_product(
    document_id: str,
    new_product: CabinetRequestModel,
    db: IRepository = Depends(get_cabinet_repository),
) -> None:
    db.update(document_id=document_id, element=new_product)
