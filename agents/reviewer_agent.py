from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:1.5b")


def reviewer_agent(state):
    article = state["article"]

    response = llm.invoke(
        f"""
        Review the following article.

        Check:
        - Clarity
        - Structure
        - Professionalism

        Article:

        {article}

        Provide a final review.
        """
    )

    return {
        "review": response.content
    }