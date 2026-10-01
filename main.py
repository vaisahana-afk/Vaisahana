from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Quickstart")


class Message(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Your FastAPI app is running!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/messages")
def create_message(message: Message):
    return {"received": message.text}