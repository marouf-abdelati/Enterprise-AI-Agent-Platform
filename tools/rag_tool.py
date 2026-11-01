from pathlib import Path
import numpy as np
import faiss

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama


def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


pdf_path =Path("data/documents/LLM.pdf")


text = load_pdf(pdf_path)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

embedding_model = SentenceTransformer(
    "paraphrase-MiniLM-L3-v2"
)

embeddings = embedding_model.encode(chunks)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings).astype("float32")
)
llm = ChatOllama(
    model="qwen2.5:1.5b"
)