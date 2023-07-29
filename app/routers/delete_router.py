from fastapi import APIRouter
from fastapi.params import Depends
from requests import codes
from app.classes.dependencies import get_product_repository, get_user_repository
from app.models.repositories.repository_interface import IRepository

from app.models.validation import FilterRequestModel


delete_router = APIRouter(prefix="/delete", tags=["delete"])


@delete_router.delete("/product", status_code=codes.NO_CONTENT)
async def delete_user(
    document_id: str = "",
    db: IRepository = Depends(get_product_repository),
) -> None:
    db.remove(document_id=document_id)
