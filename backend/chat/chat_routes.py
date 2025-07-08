from fastapi import APIRouter, Depends, HTTPException, Header
from database.connection import db
from chat.chat_model import ChatSession, ChatMessage
from auth.jwt_handler import verify_token
from utils.openrouter_client import call_openrouter
from bson import ObjectId

chat_router = APIRouter()
chats_collection = db["chats"]

def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload['sub']

@chat_router.post("/chat/create")
def create_chat(session: ChatSession, user_email=Depends(get_current_user)):
    chat_data = session.dict()
    result = chats_collection.insert_one(chat_data)
    return {"msg": "Chat created", "chat_id": str(result.inserted_id)}

@chat_router.get("/chat/list")
def list_chats(user_email=Depends(get_current_user)):
    chats = list(chats_collection.find({"user_email": user_email}))
    for c in chats:
        c["_id"] = str(c["_id"])
    return chats

@chat_router.post("/chat/send/{chat_id}")
def send_message(chat_id: str, message: ChatMessage, user_email=Depends(get_current_user)):
    from bson import ObjectId
    chat = chats_collection.find_one({"_id": ObjectId(chat_id)})
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    chat["messages"].append(message.dict())

    # Generate response from OpenRouter
    response = call_openrouter(chat["messages"])

    chat["messages"].append({"role": "assistant", "content": response})
    chats_collection.update_one({"_id": ObjectId(chat_id)}, {"$set": {"messages": chat["messages"]}})

    return {"response": response}
