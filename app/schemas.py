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

class QuizOption(BaseModel):
    A: str
    B: str
    C: str


class QuizQuestion(BaseModel):
    question: str = Field(..., description="The quiz question")
    options: QuizOption = Field(..., description="The answer options for the quiz question")
    correct_answer: str = Field(..., description="The correct answer option: 'A', 'B', or 'C'")
    explanation: str = Field(..., description="Explanation for the correct answer")

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
    total_questions: int

class QuizRequest(BaseModel):
    comments: str
    original_text: str