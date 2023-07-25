from typing import Any, Callable, TypeVar
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from requests import codes


_T = TypeVar("_T")  # any type
_I = TypeVar("_I")  # innput class
_O = TypeVar("_O")  # output class


def type_of_dict_data(
    type: _T,
    data: dict,
    error_handler: Callable,
) -> Any:
    """
    ## converting data to type and check if it is valid

    1. param type: type to convert data to
    2. param data: data to convert to type
    3. param error_handler: function to handle error

    ### returns: object instance by dictionary's data
    """

    try:
        type(**data)
    except ValidationError as e:
        error_handler()
    return type(**data)


def type_validation_check(
    request_model_class: _I, response_model_class: _O, data: dict
) -> _O:
    """
    ## checking if data from dictionary is valid for instantiation of request and response model classes

    1. param request_model_class: class of request model
    2. param response_model_class: class of response model
    3. param data: data to check

    ### returns: object of response model class
    """

    def handler():
        raise HTTPException(
            status_code=codes.BAD_REQUEST,
            detail=str("error while checking type"),
        )

    request_type = type_of_dict_data(
        request_model_class,
        data,
        error_handler=handler,
    )

    response_type = type_of_dict_data(response_model_class, data, error_handler=handler)

    return response_type
