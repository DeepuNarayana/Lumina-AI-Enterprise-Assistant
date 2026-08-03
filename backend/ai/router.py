from fastapi import APIRouter
from ai.schemas import ChatRequest, ChatResponse
#from ai.service import AIService
from app.services.chat_service import ChatService

#ai_service=AIService()
chart_service=ChatService()

router=APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post(
    "/chat"
    #response_model=ChatResponse
)
def chat(request: ChatRequest):
    response=chart_service.process(request.message)
    return response
    #response= ai_service.process_message(
     #   request.message
   # )

    # return ChatResponse(
    #     response=response
    # )