# ./backend/src/main.py

import logging
import sys
from uvicorn import run
from fastapi import FastAPI

from src.models.db import engine, BaseModel
from models.main_db import BaseModel
# from src.settings import get_settings
from src.routers.base import api_router
from src.models.some_data import insert_data_to_db

# settings = get_settings()

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.setFormatter(fmt)

logger_db = logging.getLogger("sqlalchemy")
logger_db.setLevel(logging.DEBUG)
logger_db.addHandler(logger)

app = FastAPI()

@app.on_event("startup")
def startup():
    engine.connect()
    BaseModel.metadata.create_all(engine)
    insert_data_to_db(engine)


@app.on_event("shutdown")
def shutdown():
    pass


app.include_router(api_router)


@app.get("/create_all")
def root():
    return "Hello "


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
