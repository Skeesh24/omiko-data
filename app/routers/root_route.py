from fastapi import FastAPI
from .select_router import select_router
from .insert_router import insert_router


app = FastAPI()
app.include_router(select_router)
app.include_router(insert_router)


@app.get("/")
async def read_root():
    return {"Hello, boss": "there are a database API, alright?"}
