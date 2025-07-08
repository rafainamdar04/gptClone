from fastapi import APIRouter, File, UploadFile, HTTPException
import fitz  # PyMuPDF
from utils.chroma_rag import store_pdf_embeddings, ask_question_from_pdf
from fastapi import Form

pdf_router = APIRouter()

@pdf_router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDFs are supported")

    contents = await file.read()
    text = extract_text_from_pdf(contents)
    doc_id = store_pdf_embeddings(text)
    return {"msg": "PDF uploaded and processed", "doc_id": doc_id}

@pdf_router.post("/ask-pdf/")
def ask_pdf(
    doc_id: str = Form(...),
    question: str = Form(...)
):
    answer = ask_question_from_pdf(doc_id, question)
    return {"answer": answer}

def extract_text_from_pdf(content: bytes) -> str:
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
