"""Compatibility shim: re-export agent factories and run_agent from the
new modular layout. This keeps existing imports in the codebase working.
"""

from app.agents_definitions import EditResponse, create_grammar_agent, create_clarity_agent, create_tone_agent

# The concrete Agent/Runner implementation lives outside this package
# (for example the OpenAI Agents SDK). We expose a thin run_agent wrapper
# that calls Runner.run so existing code keeps working.
from agents import Runner


async def run_agent(agent, user_input: str) -> EditResponse:
    result = await Runner.run(agent, user_input)
    return result.final_output


# Provide backward-compatible names used across the project
grammar_agent = create_grammar_agent
clarity_agent = create_clarity_agent
create_tone_agent = create_tone_agent