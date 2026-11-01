from langgraph.graph import StateGraph, END

from app.state import AgentState

from agents.manager_agent import manager_agent
from agents.research_agent import research_agent
from agents.writer_agent import writer_agent
from agents.reviewer_agent import reviewer_agent


builder = StateGraph(AgentState)

builder.add_node("manager", manager_agent)
builder.add_node("researcher", research_agent)
builder.add_node("writer", writer_agent)
builder.add_node("reviewer", reviewer_agent)

builder.set_entry_point("manager")

builder.add_edge("manager", "researcher")
builder.add_edge("researcher", END)
builder.add_edge("writer", END)

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke(
        {
            "topic": "Artificial Intelligence"
        }
    )

    print(result)