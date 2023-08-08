from app.routers.root_route import app
from uvicorn import run


if __name__ == "__main__":
    run(app, host="localhost", port=8000)
