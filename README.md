
# GPT-Style AI Chatbot Backend (FastAPI + MongoDB Atlas + LangChain + RAG)

This is the **backend** for a GPT-style AI chatbot, built using **FastAPI**, **MongoDB Atlas**, **LangChain**, and **OpenRouter**. It supports:

- 🔐 Secure user authentication (JWT)
- 💬 Persistent chat sessions (MongoDB Atlas)
- 📄 PDF upload and RAG-based question answering
- 🧠 AI completions powered by OpenRouter (Mistral-7B)
- ⚡ Local vector database using Chroma and SentenceTransformers

---

## 🚀 How to Use

### 📦 1. Clone and Navigate

```bash
git clone https://github.com/your-username/gpt-chatbot-backend.git
cd gpt-chatbot-backend/backend
````

### 🐍 2. Create and Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 📚 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Create a `.env` File

Create a `.env` file in the `backend/` folder:

```
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
ALGORITHM=HS256
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 🧠 5. Run the Server

```bash
uvicorn main:app --reload
```

## 🧪 API Overview

### 🔐 Auth Routes

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| POST   | `/auth/signup` | Register new user        |
| POST   | `/auth/login`  | Authenticate and get JWT |

### 💬 Chat Routes (Requires JWT)

| Method | Endpoint               | Description               |
| ------ | ---------------------- | ------------------------- |
| POST   | `/chat/create`         | Create a new chat session |
| GET    | `/chat/list`           | List user's chats         |
| POST   | `/chat/send/{chat_id}` | Send message, get reply   |

### 📄 PDF + RAG Routes

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | `/upload-pdf/` | Upload PDF and embed   |
| POST   | `/ask-pdf/`    | Ask question using RAG |

---
## Testing with Postman
![image](https://github.com/user-attachments/assets/75e240cf-fbec-4cdf-9526-d91998f3374e)
![image](https://github.com/user-attachments/assets/404099ba-3639-4a6b-9802-5d92a5096859)
![image](https://github.com/user-attachments/assets/5b48112c-19f1-448f-85fc-08a3962b604c)
![image](https://github.com/user-attachments/assets/fbcfe859-b847-4b48-8cf2-5eca4c5a863c)
![image](https://github.com/user-attachments/assets/3deaa830-6713-404f-a1af-2dfbd6b852fa)


## 🛠 Built With

* [FastAPI](https://fastapi.tiangolo.com/) — API framework
* [MongoDB Atlas](https://www.mongodb.com/try/download/community) — database for users and chats
* [LangChain](https://www.langchain.com/) — RAG pipeline
* [Chroma](https://www.trychroma.com/) — vector store
* [SentenceTransformers](https://www.sbert.net/) — MiniLM embeddings
* [OpenRouter](https://openrouter.ai/) — LLM completions (Mistral-7B)

---
