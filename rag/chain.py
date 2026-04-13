# chain.py
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Tongyi
from .retriever import retrieve_chunks

load_dotenv()

PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}

---
Question: {question}
"""

def query(question: str, selected_file: str = "All documents"):
    results = retrieve_chunks(question, selected_file)
    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context, question=question)
    model = Tongyi(
        model_name="qwen-turbo",
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
    )
    response = model.invoke(prompt)
    sources = [doc.metadata.get("source") for doc, score in results]
    return response, sources