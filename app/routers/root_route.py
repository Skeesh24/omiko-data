from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .select_router import select_router
from .insert_router import insert_router
from .update_router import put_router
from .delete_router import delete_router

from app.database.firebase import initialize


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "https://omiko-api-deploy.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(select_router)
app.include_router(insert_router)
app.include_router(put_router)
app.include_router(delete_router)


# db init
initialize()


@app.get("/")
async def read_root():
    return {"Hello, boss": "there are a database API, alright?"}
