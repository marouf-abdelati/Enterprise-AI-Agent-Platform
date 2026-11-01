from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:1.5b")

def manager_agent(state):

    topic = state["topic"]

    return {
        "plan": f"""
1. Understand {topic}
2. Identify key concepts
3. Analyze applications and challenges
"""
    }

    return {
        "plan": response.content
    }