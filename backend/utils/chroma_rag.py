from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import uuid

# Set up the Chroma DB directory
persist_directory = "chroma_store"

# Use a free local embedding model
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def store_pdf_embeddings(text: str) -> str:
    # Chunk the extracted text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    chunks = text_splitter.create_documents([text])

    # Create a unique document collection
    doc_id = str(uuid.uuid4())
    vectordb = Chroma(
        collection_name=doc_id,
        embedding_function=embedding,
        persist_directory=persist_directory
    )
    vectordb.add_documents(chunks)
    vectordb.persist()
    return doc_id

def ask_question_from_pdf(doc_id: str, question: str) -> str:
    vectordb = Chroma(
        collection_name=doc_id,
        embedding_function=embedding,
        persist_directory=persist_directory
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    docs = retriever.get_relevant_documents(question)

    # Combine relevant context chunks
    context = "\n".join([doc.page_content for doc in docs])
    prompt = [
        {"role": "system", "content": "Use the context below to answer the user's question. If the answer isn't in the context, say 'I don’t know.'\n\n" + context},
        {"role": "user", "content": question}
    ]

    from utils.openrouter_client import call_openrouter
    return call_openrouter(prompt)
