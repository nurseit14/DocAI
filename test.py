from dotenv import load_dotenv
import os

load_dotenv()

from rag.loader import load_documents
from rag.chunker import split_text
from rag.embedder import create_vectorstore
from rag.retriever import retrieve_chunks
from rag.chain import query

# Step 1 - Load
docs = load_documents()

# Step 2 - Chunk
chunks = split_text(docs)
print(f"Created {len(chunks)} chunks")

# Step 3 - Embed & Save
create_vectorstore(chunks)

# Step 4,5 - Retireve the results
question = "What are the advantages of e-assessment according to students?"
response, sources = query(question)

print(f"\nAnswer: {response}")
print(f"\nSources: {sources}")


