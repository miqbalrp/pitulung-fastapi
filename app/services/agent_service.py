from typing import Callable, Optional
from pydantic import BaseModel
from app.agents_definitions import (
    EditResponse, 
    QuizResponse,
    create_grammar_agent, 
    create_clarity_agent, 
    create_tone_agent, 
    create_quiz_agent
)

# Import the project's Agent/Runner implementation. Keep this import local so we can
# shim or mock it in tests if needed.
from agents import Agent, Runner


class AgentService:
    def __init__(self, agent_factory: Callable = Agent):
        self.agent_factory = agent_factory

    async def run_agent(self, agent: Agent, text: str) -> EditResponse:
        result = await Runner.run(agent, text)
        # result.final_output is expected to be a pydantic model (EditResponse)
        return result.final_output

    async def run_steps(self, steps: list, text: str) -> tuple[str, dict]:
        current_text = text
        comments = {}

        for step in steps:
            if step == "grammar":
                agent = create_grammar_agent(self.agent_factory)
                res = await self.run_agent(agent, current_text)
                current_text = res.edited_text
                comments["grammar"] = res.comments or ""

            elif step == "clarity":
                agent = create_clarity_agent(self.agent_factory)
                res = await self.run_agent(agent, current_text)
                current_text = res.edited_text
                comments["clarity"] = res.comments or ""

            elif step.startswith("tone:"):
                tone = step.split(":", 1)[1]
                agent = create_tone_agent(self.agent_factory, tone)
                res = await self.run_agent(agent, current_text)
                current_text = res.edited_text
                comments["tone"] = res.comments or ""

        return current_text, comments

    async def run_quiz_from_grammar(self, grammar_comments: str, original_text: str, number_of_questions: int=5) -> QuizResponse:
        """Generate quiz based on grammar agent's comments"""
        agent = create_quiz_agent(self.agent_factory)
        res = await self.run_agent(agent, f"Original text: {original_text}\n\nGrammar corrections: {grammar_comments}\n\nGenerate {number_of_questions} quiz questions.")
        return res

_service: Optional[AgentService] = None

def get_agent_service() -> AgentService:
    global _service
    if _service is None:
        _service = AgentService()
    return _service
