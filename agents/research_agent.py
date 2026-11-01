from tools.rag_tool import llm
from tools.rag_tool import embedding_model
from tools.rag_tool import index
from tools.rag_tool import chunks

import numpy as np


def research_agent(state):

    topic = state["topic"]
    plan = state["plan"]

    query_embedding = embedding_model.encode([topic])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    retrieved_chunks = []

    for i in indices[0]:
        retrieved_chunks.append(
            f"[CHUNK {i}]\n{chunks[i]}"
        )

    context = "\n\n".join(retrieved_chunks)

    response = llm.invoke(
        f"""
        You are a professional AI Research      Use ONLY the provided context.

        Context:
        {context}

        Research Plan:
        {plan}

        Topic:
        {topic}

        Create a structured research report with:

        1. Executive Summary
        2. Key Findings
        3. Important Concepts
        4. Real-World Applications
        5. Conclusion

        At the end add:

        Sources:
        - CHUNK IDs used

        Do not copy the text directly.
        Summarize and explain it professionally.
        """
    )

    return {
        "research": response.content
    }