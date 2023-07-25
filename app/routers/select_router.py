from fastapi import APIRouter

from app.models.validation import FilterRequestModel
from fastapi.params import Depends
from fireo.database import Database

from app.database.firebase import get_db
from app.models.validation import FilterRequestModel


select_router = APIRouter(prefix="/select", tags=["select", "get"])


@select_router.get("/{tablename}")
async def select(
    tablename: str,
    limit: int = 5,
    offset: int = 0,
    where: FilterRequestModel = None,
    db: Database = Depends(get_db),
) -> list[dict]:
    # replace this connection with a repository call
    table = db.conn.collection(tablename)
    query = table.limit(limit).offset(offset)
    if where:
        query = query.where(**where.dict(exclude_defaults=True))
    return [x.to_dict() for x in query.get()]
