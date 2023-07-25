from typing import TypeVar, Generic

from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from requests import codes


class UserResponseModel(BaseModel):
    email: str


_T = TypeVar("_T")


def type_validation_check(request_model_class: Generic[_T], data: dict) -> _T:
    try:
        obj = request_model_class(**data)
    except ValidationError as e:
        raise HTTPException(
            status_code=codes.bad_request, detail=str("Invalid request")
        )
    return obj


