from fastapi import HTTPException, status


def try_get_repository(uow, tablename):
    try:
        return uow.__getattribute__(tablename)
    except:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail=tablename)


def is_list(elements):
    try:
        return len(elements) >= 0
    except:
        return False
