from fastapi import HTTPException
from httpx import codes


def try_get_repository(uow, tablename):
    try:
        return uow.__getattribute__(tablename)
    except:
        raise HTTPException(codes.UNPROCESSABLE_ENTITY, detail=tablename)


def is_list(elements):
    try:
        return len(elements) >= 0
    except:
        return False
