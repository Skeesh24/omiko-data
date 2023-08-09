from fastapi import APIRouter
from fastapi.params import Depends
from requests import codes
from app.classes.dependencies import (
    get_uow,
)
from app.classes.functions import try_get_repository
from app.models.repositories.repository_interface import IRepository


delete_router = APIRouter(prefix="/delete", tags=["delete"])


@delete_router.delete("/{tablename}", status_code=codes.NO_CONTENT)
async def delete_user(
    tablename: str,
    document_id: str = "",
    uow=Depends(get_uow),
) -> None:
    db: IRepository = try_get_repository(uow, tablename)
    db.remove(document_id=document_id)
