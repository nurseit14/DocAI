# loader.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import CSVLoader
DATA_PATH = "data/"


def load_single_file(file_path: str):
    """
  Load a single file based on its extension.
  Returns a list of Document objects.
  """
    ext = file_path.split(".")[-1].lower()

    if ext == "pdf":
        loader = PyPDFLoader(file_path)  # PyPDFLoader(file_path)
    elif ext == "docx":
        loader =  Docx2txtLoader(file_path)
    elif ext == "txt":
        loader = TextLoader(file_path)
    elif ext == "csv":
        loader = CSVLoader(file_path)
    else:
        print(f"Unsupported file type: {ext}")
        return []

    return loader.load()


def load_documents():
  all_docs = []

  for filename in os.listdir(DATA_PATH):
    if filename.startswith("."):  # ← skip hidden files
      continue
    file_path = os.path.join(DATA_PATH, filename)
    print(f"Loading: {filename}")
    docs = load_single_file(file_path)
    all_docs.extend(docs)

  print(f"Loaded {len(all_docs)} documents total.")
  return all_docs