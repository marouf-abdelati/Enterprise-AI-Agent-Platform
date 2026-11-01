from typing import TypedDict


class AgentState(TypedDict):
    topic: str
    plan: str
    research: str
    article: str
    review: str
