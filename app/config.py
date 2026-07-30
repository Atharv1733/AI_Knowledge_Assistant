from dotenv import load_dotenv
import os

load_dotenv()

# Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = "gemini-3.6-flash"

# Embedding Model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Reranker Model
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# Retrieval
TOP_K = 5
FAISS_SEARCH_K = 20

# Data Paths
FAISS_INDEX_PATH = "data/faiss_index.bin"
CHUNKS_PATH = "data/chunks.pkl"