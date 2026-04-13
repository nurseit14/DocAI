# DocAI 🤖📄

> Chat with your documents using AI. Upload PDFs, Word files, CSVs, or text files and ask questions about them in natural language.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-latest-purple)

---

## 🚀 Features

- 📁 **Multi-file upload** — Upload multiple documents at once
- 📄 **Multiple file types** — Supports PDF, DOCX, TXT, and CSV
- 🔍 **Semantic search** — Finds the most relevant parts of your documents
- 💬 **Chat interface** — Natural conversation with your documents
- 🎯 **Document filtering** — Ask questions about a specific document or all documents at once
- 🗂️ **Database viewer** — See which files are currently indexed
- 🔒 **Fully local embeddings** — Uses HuggingFace embeddings, no data sent to external servers
- ⚡ **Powered by Qwen** — Fast and accurate answers via Qwen API

---

## 🧠 How It Works

```
Upload Document
      ↓
Split into chunks (LangChain)
      ↓
Generate embeddings (HuggingFace all-MiniLM-L6-v2)
      ↓
Store in vector database (ChromaDB)
      ↓
User asks a question
      ↓
Find most relevant chunks (similarity search)
      ↓
Generate answer with sources (Qwen API)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Document Loading | LangChain Community Loaders |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| LLM | Qwen (via DashScope API) |
| Language | Python 3.9+ |

---

## 📁 Project Structure

```
DocAI/
├── app.py               # Streamlit UI
├── test.py              # Testing script
├── requirements.txt     # Dependencies
├── .env                 # API keys (not committed)
├── data/                # Uploaded documents (not committed)
├── chroma_db/           # Vector database (not committed)
└── rag/
    ├── __init__.py
    ├── loader.py        # Document loading (PDF, DOCX, TXT, CSV)
    ├── chunker.py       # Text splitting
    ├── embedder.py      # Embeddings + ChromaDB storage
    ├── retriever.py     # Semantic search
    └── chain.py         # LLM integration + prompt
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/DocAI.git
cd DocAI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:
```
DASHSCOPE_API_KEY=your_qwen_api_key_here
```
Get your free API key at [dashscope.aliyuncs.com](https://dashscope.aliyuncs.com)

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📖 Usage

1. **Upload documents** — Use the sidebar to upload one or more files (PDF, DOCX, TXT, CSV)
2. **Process** — Click the "⚙️ Process Documents" button
3. **Select scope** — Choose to ask about all documents or a specific one
4. **Ask questions** — Type your question in the chat input
5. **Get answers** — DocAI returns an answer with the source documents cited

---

## 📦 Requirements

```
streamlit
langchain
langchain-community
langchain-openai
langchain-huggingface
langchain-text-splitters
langchain-core
chromadb
pypdf
docx2txt
sentence-transformers
python-dotenv
dashscope
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🗺️ Roadmap

- [ ] Image support (OCR with Tesseract)
- [ ] Web URL loading
- [ ] Delete specific documents from database
- [ ] Export chat history
- [ ] Support for more LLM providers (OpenAI, Anthropic)

---

## 👨‍💻 Author

Built by **Nursei Itzhuzbay**

---

## 📄 License

MIT License — feel free to use and modify this project.
