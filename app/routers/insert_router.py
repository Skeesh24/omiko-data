from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database

from app.database.firebase import get_db


insert_router = APIRouter(prefix="/insert", tags=["insert", "post"])


@insert_router.post("/{tablename}", status_code=codes.created)
async def insert(tablename: str, data: dict = Body(), db: Database = Depends(get_db)):
    ins = db.conn.collection(tablename).add(data)
    print(ins)
