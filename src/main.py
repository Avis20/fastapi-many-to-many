from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
def hello_world():
    return "hello"


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
