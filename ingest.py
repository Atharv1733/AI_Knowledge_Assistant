import os
import pickle
import fitz
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

DOCUMENTS_PATH = "documents"
DATA_PATH = "data"

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def chunk_text(text, chunk_size=500):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(
            " ".join(words[i:i + chunk_size])
        )

    return chunks


def ingest_documents():

    all_chunks = []
    embeddings = []

    for filename in os.listdir(DOCUMENTS_PATH):

        if not filename.endswith(".pdf"):
            continue

        pdf_path = os.path.join(
            DOCUMENTS_PATH,
            filename
        )

        print(f"Processing {filename}")

        doc = fitz.open(pdf_path)

        for page_number, page in enumerate(doc):

            text = page.get_text()

            chunks = chunk_text(text)

            for chunk in chunks:

                embedding = embedding_model.encode(chunk)

                embeddings.append(embedding)

                all_chunks.append(
                    {
                        "text": chunk,
                        "source": filename,
                        "page": page_number + 1
                    }
                )

        doc.close()

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(embeddings)

    os.makedirs(DATA_PATH, exist_ok=True)

    faiss.write_index(
        index,
        "data/faiss_index.bin"
    )

    with open(
        "data/chunks.pkl",
        "wb"
    ) as file:

        pickle.dump(
            all_chunks,
            file
        )

    print()
    print("Total Chunks :", len(all_chunks))
    print("Index Saved Successfully")


if __name__ == "__main__":
    ingest_documents()