from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello Ian"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User ID is {user_id}"
    }


@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {
        "keyword": keyword,
        "limit": limit
    }