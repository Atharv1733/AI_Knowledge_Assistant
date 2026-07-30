from fastapi import APIRouter 

from app.schemas.chat_schema import ChatRequest, ChatResponse 
from app.services.chat_service import get_answer 

router = APIRouter() 

@router.post("/chat", response_model=ChatResponse) 
def chat(request: ChatRequest): 
    return get_answer(request.question)