from fastapi import FastAPI
from pydantic import BaseModel

from app.main import graph

app = FastAPI(
    title="Enterprise AI Agent Platform API",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Agent Platform API is running"
    }


@app.post("/ask")
def ask(request: QueryRequest):

    result = graph.invoke(
        {
            "topic": request.question
        }
    )

    return {
        "plan": result.get("plan", ""),
        "answer": result.get("research", "")
    }