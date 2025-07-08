from fastapi import FastAPI
from auth.auth_routes import router as auth_router
from chat.chat_routes import chat_router
from pdf.pdf_routes import pdf_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")
app.include_router(pdf_router)
