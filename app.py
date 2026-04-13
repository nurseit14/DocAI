import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HOME"] = os.path.expanduser("~/hf_cache")

import streamlit as st
from rag.loader import load_documents
from rag.chunker import split_text
from rag.embedder import create_vectorstore
from rag.chain import query
from rag.embedder import get_indexed_files

st.title("📄 Document RAG Q&A")
st.write("Upload documents and ask questions about these documents.")

with st.sidebar:
    st.header("📂 Upload Document")
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "docx", "txt", "csv"],
        accept_multiple_files=True,
    )

    process_button = st.button("⚙️ Process Documents")

    if uploaded_files and process_button:
        with st.spinner("Processing your documents..."):
            for uploaded_file in uploaded_files:
                with open(f"data/{uploaded_file.name}", "wb") as f:
                    f.write(uploaded_file.getbuffer())
            docs = load_documents()
            chunks = split_text(docs)
            create_vectorstore(chunks)
        st.success("✅ Ready! Ask a question below.")

    st.subheader("📁 Files in database:")
    indexed_files = get_indexed_files()
    for file in indexed_files:
        st.write(f"• {file}")

    selected_file = st.selectbox(
        "🔍 Ask about:",
        options=["All documents"] + list(indexed_files)
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if question := st.chat_input("Ask a question about your document..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # Get answer
    with st.spinner("Thinking..."):
        response, sources = query(question, selected_file=selected_file)

    # Show assistant answer
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
        st.caption(f"📚 Sources: {set(sources)}")