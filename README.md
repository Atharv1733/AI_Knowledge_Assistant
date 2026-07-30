# 🤖 AI Knowledge Assistant

An AI-powered Knowledge Assistant that allows users to upload PDF documents, build a vector database, and ask questions using Retrieval-Augmented Generation (RAG).

---

## Features

- Upload PDF documents
- Automatic document ingestion
- FAISS vector database
- SentenceTransformer embeddings
- CrossEncoder reranking
- Google Gemini LLM
- Streamlit chat interface
- FastAPI backend
- Source citations

---

## Tech Stack

### Backend
- FastAPI

### Frontend
- Streamlit

### LLM
- Google Gemini

### Embedding Model
- all-MiniLM-L6-v2

### Reranker
- cross-encoder/ms-marco-MiniLM-L-6-v2

### Vector Database
- FAISS

### PDF Processing
- PyMuPDF

---

## Project Structure

```
AI_Knowledge_Assistant
│
├── app
│   ├── config.py
│   ├── main.py
│   ├── routes
│   └── services
│
├── data
├── documents
├── ingest.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run FastAPI

```bash
python -m uvicorn app.main:app --reload
```

FastAPI:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## Workflow

1. Upload PDF documents.
2. Documents are processed.
3. Embeddings are generated.
4. FAISS index is created.
5. User asks a question.
6. Relevant chunks are retrieved.
7. CrossEncoder reranks results.
8. Gemini generates the final answer.
9. Sources are displayed.

---

## Author

Atharv Gadhave