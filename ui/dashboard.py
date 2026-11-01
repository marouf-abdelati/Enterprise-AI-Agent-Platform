import streamlit as st

import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.append(str(root))

from app.main import graph

st.set_page_config(
    page_title="Enterprise AI Agent Platform",
    page_icon="🤖",
    layout="wide"
)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("🤖 Enterprise AI Agent Platform")

with st.sidebar:

    st.header("Platform Info")

    st.metric("Agents", "2")
    st.metric("Model", "Qwen 2.5")
    st.metric("RAG", "Enabled")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)
question = st.text_input(
    "Ask a question",
    placeholder="What is RAG?"
)

docs_dir = Path("data/documents")
docs_dir.mkdir(parents=True, exist_ok=True)


if st.button("Generate"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()
    
    with st.spinner("Running Multi-Agent Workflow..."):

        if uploaded_files:
            for uploaded_file in uploaded_files:

                with open(
                    f"data/documents/{uploaded_file.name}",
                    "wb"
                ) as f:
            
                    f.write(
                        uploaded_file.getbuffer()
                    )

        result = graph.invoke(
            {
                "topic": question
            }
        )

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": result["research"]
            }
        )


    st.subheader("💬 Answer")
    st.write(result.get("research", "No answer generated"))


st.subheader("📝 History")
for item in st.session_state.chat_history:

    st.markdown(
        f"**Q:** {item['question']}"
    )

    st.markdown(
        f"**A:** {item['answer']}"
    )

