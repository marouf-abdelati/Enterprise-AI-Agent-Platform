from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content + "\n"

    return text


pdf_path = Path("data/documents/uploaded.pdf")

text = load_pdf(pdf_path)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings).astype("float32")
)

question = "What is RAG?"

query_embedding = model.encode([question])

distances, indices = index.search(
    np.array(query_embedding).astype("float32"),
    k=3
)

print("\nTOP RESULTS:\n")

for i in indices[0]:
    print("-" * 80)
    print(chunks[i])