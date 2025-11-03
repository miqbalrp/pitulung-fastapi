from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ImproveRequest(BaseModel):
    text: str
    steps: List[str]

class ImproveResponse(BaseModel):
    improved_text: str
    comments: Dict[str, str]

class EditResponse(BaseModel):
    edited_text: str = Field(
        ..., 
        description="The edited version of the input text, formatted in markdown. Use markdown to highlight changes, corrections, or suggestions."
    )
    comments: Optional[str] = Field(
        None, 
        description="Clear and educative comments or suggestions regarding the edits made, formatted in markdown."
    )