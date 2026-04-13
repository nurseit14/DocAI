#embedder.py

import os
os.environ["HF_HOME"] = os.path.expanduser("~/hf_cache")

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
import shutil


def create_vectorstore(chunks, persist_dir="./chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    print(f"Saved {len(chunks)} chunks to ChromaDB at {persist_dir}")
    return vectorstore
def get_indexed_files():
    import chromadb
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_collection("langchain")
        results = collection.get(include=["metadatas"])
        sources = set()
        for metadata in results["metadatas"]:
            if "source" in metadata:
                sources.add(metadata["source"])
        return sources
    except Exception:
        return set()  # return empty set if collection doesn't exist yet
