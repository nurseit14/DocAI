import os
os.environ["HF_HOME"] = os.path.expanduser("~/hf_cache")

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "./chroma_db"

def retrieve_chunks(question: str, selected_file: str ="All documents",  k: int = 3,):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    if selected_file == "All documents":
        results = db.similarity_search_with_relevance_scores(question, k=k)
    else:
        results = db.similarity_search_with_relevance_scores(
            question,k=k,
            filter = {"source": selected_file}
        )
    return results