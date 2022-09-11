from fastapi import FastAPI
from uvicorn import run

from src.models.base import engine, BaseModel
from src.settings import get_settings

settings = get_settings()

app = FastAPI()


@app.get("/")
def hello_world():
    return "hello"


@app.on_event("startup")
def startup():
    engine.connect()
    BaseModel.metadata.create_all(engine)


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
