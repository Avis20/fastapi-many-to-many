# ./src/main.py

from fastapi import FastAPI
from uvicorn import run

from src.models.main_db import engine
from src.settings import get_settings
from src.routers.base import router as base_router

settings = get_settings()

app = FastAPI()
app.include_router(base_router)


@app.get("/")
def hello_world():
    return "hello"


@app.on_event("startup")
def startup():
    engine.connect()


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
