from fastapi import APIRouter
from fastapi.params import Depends
from requests import codes
from app.classes.dependencies import (
    get_cabinet_repository,
    get_office_repository,
    get_order_repository,
    get_product_category_repository,
    get_product_repository,
    get_user_repository,
)
from app.models.repositories.repository_interface import IRepository

from app.models.validation import FilterRequestModel


delete_router = APIRouter(prefix="/delete", tags=["delete"])


@delete_router.delete("/user", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_user_repository),
) -> None:
    db.remove(document_id=document_id)


@delete_router.delete("/product", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_product_repository),
) -> None:
    db.remove(document_id=document_id)


@delete_router.delete("/order", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_order_repository),
) -> None:
    db.remove(document_id=document_id)


@delete_router.delete("/product_category", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_product_category_repository),
) -> None:
    db.remove(document_id=document_id)


@delete_router.delete("/office", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_office_repository),
) -> None:
    db.remove(document_id=document_id)


@delete_router.delete("/cabinet", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_cabinet_repository),
) -> None:
    db.remove(document_id=document_id)
