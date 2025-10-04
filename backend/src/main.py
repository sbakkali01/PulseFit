from typing import Union

from fastapi import FastAPI

from exercise import exercises

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/exercises")
def get_all_exercises():
    return exercises


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}