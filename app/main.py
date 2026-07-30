from fastapi import FastAPI

from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from app.routes.documents import router as documents_router

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(documents_router)


@app.get("/")
def home():
    return {
        "status": "running"
    }