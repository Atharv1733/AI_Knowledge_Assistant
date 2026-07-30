import faiss
import pickle
import numpy as np

from sentence_transformers import (
    SentenceTransformer,
    CrossEncoder,
)

from app.config import (
    EMBEDDING_MODEL,
    RERANKER_MODEL,
    TOP_K,
    FAISS_SEARCH_K,
    FAISS_INDEX_PATH,
    CHUNKS_PATH,
)

# Load embedding model
embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)

# Load reranker model
reranker = CrossEncoder(
    RERANKER_MODEL
)

# Load FAISS index and chunks
try:

    index = faiss.read_index(
        FAISS_INDEX_PATH
    )

    with open(CHUNKS_PATH, "rb") as file:
        chunks = pickle.load(file)

except FileNotFoundError:

    raise Exception(
        "Knowledge base not found. Please upload and process PDF documents first."
    )

except Exception as e:

    raise Exception(
        f"Failed to load knowledge base: {e}"
    )


def retrieve_context(question: str, top_k: int = TOP_K):

    # Convert question to embedding
    question_embedding = embedding_model.encode([question])

    # Retrieve candidate chunks
    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        FAISS_SEARCH_K
    )

    candidates = []

    for idx in indices[0]:

        if idx == -1:
            continue

        candidates.append(chunks[idx])

    if not candidates:
        return []

    # Prepare question-chunk pairs
    pairs = [
        (question, chunk["text"])
        for chunk in candidates
    ]

    # Rerank
    scores = reranker.predict(pairs)

    ranked_chunks = sorted(
        zip(scores, candidates),
        key=lambda x: x[0],
        reverse=True
    )

    return [
        chunk
        for score, chunk in ranked_chunks[:top_k]
    ]


if __name__ == "__main__":

    results = retrieve_context(
        "What is FastAPI?"
    )

    for i, chunk in enumerate(results):

        print("\n" + "=" * 80)
        print(f"Chunk {i + 1}\n")

        print(chunk["text"])
        print()
        print("Source:", chunk["source"])
        print("Page:", chunk["page"])