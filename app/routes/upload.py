from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File

from ingest import ingest_documents

router = APIRouter()

DOCUMENTS_DIR = Path("documents")


@router.post("/upload")
async def upload_documents(
    files: list[UploadFile] = File(...)
):

    DOCUMENTS_DIR.mkdir(exist_ok=True)

    uploaded_files = []

    for file in files:

        if not file.filename.lower().endswith(".pdf"):
            continue

        destination = DOCUMENTS_DIR / file.filename

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploaded_files.append(file.filename)

    # Rebuild FAISS Index
    ingest_documents()

    return {
        "message": "Documents processed successfully.",
        "uploaded_files": uploaded_files
    }