from fastapi import FastAPI
from fastapi.params import Depends
from fireo.database import Database

from app.database.firebase import get_db


app = FastAPI()


class firebase_filter:
    field_path: str
    op_string: str
    value: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get/{tablename}")
async def select(
    tablename: str,
    limit: int = 0,
    offset: int = 0,
    where: firebase_filter = None,
    db: Database = Depends(get_db),
) -> list[dict]:
    table = db.conn.collection(tablename)
    l = [x.to_dict() for x in table.limit(limit).offset(offset).where(**where).get()]
    return l
