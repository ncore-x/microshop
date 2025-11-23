from fastapi import FastAPI

from pydantic import EmailStr, BaseModel
import uvicorn


app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def main():
    return {"message": "Hello world!"}


@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.post("/calc/res")
def calculate(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a+b
    }


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.get("/items/")
def list_items():
    return [
        "item1",
        "item2",
        "item3",
    ]


@app.get("/items/latest")
def get_items_latest():
    return {
        "items":
            {"id": "0", "name": "latest"}
    }


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
