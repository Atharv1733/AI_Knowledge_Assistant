from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

DOCUMENTS_DIR = Path("documents")


@router.get("/documents")
def get_documents():

    if not DOCUMENTS_DIR.exists():
        return {"documents": []}

    pdfs = [
        file.name
        for file in DOCUMENTS_DIR.glob("*.pdf")
    ]

    return {
        "documents": sorted(pdfs)
    }