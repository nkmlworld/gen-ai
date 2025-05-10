# gen-ai
# 🧠 Local Retrieval-Augmented Generation (RAG) App — Basic (No Agent)

This is a basic Retrieval-Augmented Generation (RAG) app that runs entirely on a local machine. It processes PDF, generates vector embeddings using an open-source model, stores them in a local FAISS vector store, and answers questions using relevant document chunks and a local or open-source LLM.

---

## 🔧 Tech Stack

- **Python 3.10**
- **LangChain**
- **FAISS** (local vector store)
- **PyPDF / extract-msg** (document parsing)
- **Hugging Face Transformers** (embedding & LLM models)
- **Streamlit** *(optional UI)*

---

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

2. Add Documents
Place your .pdf in the data/ folder.

streamlit run app.py
