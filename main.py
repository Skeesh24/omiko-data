from app.database.firebase import initialize as db_initialize
from app.routers.root_route import app
from uvicorn import run


if __name__ == "__main__":
    db_initialize()
    # run(app, host="localhost", port=8000)
