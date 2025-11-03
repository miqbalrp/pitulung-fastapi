from fastapi import APIRouter, Depends, HTTPException
from app.schemas import ImproveRequest, ImproveResponse
from app.services.agent_service import AgentService, get_agent_service
import os

router = APIRouter()


@router.post("/improve", response_model=ImproveResponse)
async def improve_text(request: ImproveRequest, svc: AgentService = Depends(get_agent_service)):
    if not request.text or request.text.strip() == "":
        raise HTTPException(status_code=400, detail="Text is required")

    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")

    improved_text, comments = await svc.run_steps(request.steps, request.text)

    return ImproveResponse(improved_text=improved_text, comments=comments)
