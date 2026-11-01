from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


def writer_agent(state):
    research = state["research"]

    response = llm.invoke(
        f"""
        Based on the following research:

        {research}

        Write a professional article with:
        - Introduction
        - Main Content
        - Conclusion
        """
    )

    return {
        "article": response.content
    }