from fastapi import APIRouter, Depends, HTTPException
from app.schemas import *
from app.services.agent_service import AgentService, get_agent_service
import os

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, agent_service: AgentService = Depends(get_agent_service)):
    response = await agent_service.process_chat_request(request)
    return response