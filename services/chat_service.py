def build_chat_reply(message: str, user_name: str) -> str:
    if message.lower() == "hello":
        return f"Hi {user_name}, nice to meet you"

    return f"Hi {user_name}, you said: {message}"