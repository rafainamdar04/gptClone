from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatSession(BaseModel):
    user_email: str
    title: str
    messages: List[ChatMessage]
