from fastapi import APIRouter, Body
from fastapi.params import Depends
from requests.status_codes import codes
from fireo.database import Database
from fastapi.exceptions import HTTPException

from app.database.firebase import get_db
from app.models.fastapi_models import UserRequestModel, UserResponseModel


insert_router = APIRouter(prefix="/insert", tags=["insert", "post"])


@insert_router.post(
    "/{tablename}", status_code=codes.created, response_model=UserResponseModel
)
async def insert(tablename: str, data: dict = Body(), db: Database = Depends(get_db)):
    try:
        UserRequestModel(**data)
    except Exception as e:                                # TODO clear e
        raise HTTPException(status_code=codes.bad_request, detail=str(e))  
    db.conn.collection(tablename).add(data)
    return UserResponseModel(**data)
