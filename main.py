from fastapi import FastAPI
from pydantic import BaseModel

from services.chat_service import build_chat_reply

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_name: str = "Guest"

class ChatResponse(BaseModel):
    reply: str

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

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = build_chat_reply(request.message, request.user_name)

    return {
        "reply": reply
    }