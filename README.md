🤖 Enterprise AI Agent Platform
A production-ready AI platform integrating Multi-Agent Workflows, Retrieval-Augmented Generation (RAG), FAISS vector search, Ollama local LLMs, FastAPI APIs, Docker deployment and Streamlit interfaces.

🚀 Features
Multi-Agent Architecture with LangGraph
Retrieval-Augmented Generation (RAG)
Multi-PDF Knowledge Base
FAISS Vector Search
Ollama + Qwen 2.5
Source Citations
Chat History
Streamlit Interface
FastAPI Backend
Docker Deployment
🛠️ Tech Stack
Python
Streamlit
FastAPI
LangGraph
LangChain
Ollama
Qwen 2.5
FAISS
Docker
▶️ Run
streamlit run ui/dashboard.py
🌐 API
uvicorn app.api:app --reload
🐳 Docker
docker build -t enterprise-ai-agent-platform .
docker run -p 8501:8501 enterprise-ai-agent-platform
👨‍💻 Author
Marouf Abdelati