from fastapi import APIRouter

from app.services.chat_service import ChatService

router=APIRouter()

chat_service= ChatService()

@router.post("/chat")
def chat(
    message: str
):
    return chat_service.process(message)