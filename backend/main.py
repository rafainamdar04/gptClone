from fastapi import FastAPI
from auth.auth_routes import router as auth_router
from chat.chat_routes import chat_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(chat_router)
