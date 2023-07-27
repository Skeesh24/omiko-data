from typing import Any, Callable, TypeVar
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from requests import codes


_T = TypeVar("_T")  # any type


def type_of_dict_data(
    type: _T,
    data: dict,
    error_handler: Callable,
) -> Any:
    """
    ## converting dictionary data to instance of _T type or raises an exception

    1. param type: type to convert data to
    2. param data: data to convert to type
    3. param error_handler: some acrions in the error case

    ### returns: object instance by dictionary's data
    """

    try:
        type(**data)
    except ValidationError as e:
        error_handler()
    return type(**data)


def type_validation_check(type: _T, data: dict) -> _T:
    """
    ## checking if data from dictionary is valid for instantiation of _T type and raises an HTTP exception if it is not

    1. param type: class of request model
    2. param data: data to check

    ### returns: object of param's class
    """

    def handler():
        raise HTTPException(
            status_code=codes.BAD_REQUEST,
            detail=str("error while checking type"),
        )

    request_type: _T = type_of_dict_data(
        type,
        data,
        error_handler=handler,
    )

    return request_type
