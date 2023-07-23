from fastapi import APIRouter

from app.models.fastapi_models import FilterRequestModel
from fastapi.params import Depends
from fireo.database import Database

from app.database.firebase import get_db
from app.models.fastapi_models import FilterRequestModel


select_router = APIRouter(prefix="/select", tags=["select", "get"])


@select_router.get("/{tablename}")
async def select(
    tablename: str,
    limit: int = 5,
    offset: int = 0,
    where: FilterRequestModel = None,
    db: Database = Depends(get_db),
) -> list[dict]:
    table = db.conn.collection(tablename)
    query = table.limit(limit).offset(offset)
    if where:
        query = query.where(**where.__dict__)
    return [x.to_dict() for x in query.get()]
