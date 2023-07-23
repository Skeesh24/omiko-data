from fastapi import FastAPI
from fastapi.params import Depends
from fireo.database import Database

from app.database.firebase import get_db


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get/{tablename}")
async def select(tablename: str, db: Database = Depends(get_db)) -> dict:
    return db.conn.collection(tablename).limit(1).get()[0].to_dict()
