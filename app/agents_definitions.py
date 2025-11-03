from app.schemas import EditResponse

def create_grammar_agent(agent_factory):
    return agent_factory(
        name="Grammar Fixer",
        instructions=(
            "You are a grammar correction assistant. "
            "Correct all grammar, spelling, and punctuation errors without changing the tone, meaning, or writing style. "
            "Keep word choice and sentence structure unless necessary for correctness."
        ),
        output_type=EditResponse
    )


def create_clarity_agent(agent_factory):
    return agent_factory(
        name="Clarity Improver",
        instructions=(
            "You are a clarity improvement assistant. "
            "Rewrite sentences only when they are confusing, wordy, or ambiguous. "
            "Preserve the author’s tone and intent. Avoid adding new ideas."
        ),
        output_type=EditResponse
    )


def create_tone_agent(agent_factory, tone: str):
    return agent_factory(
        name=f"Tone Adjuster - {tone}",
        instructions=(
            f"You are a tone adjustment assistant. Rewrite text to match the requested tone: {tone}. "
            "Do not change the meaning. Keep vocabulary level and style consistent with the original writer unless tone requires otherwise."
        ),
        output_type=EditResponse
    )
