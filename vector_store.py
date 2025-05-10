from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

data_path=r"data"
def load_docs(data_path):
    all_docs  = []
    
    for file_name in os.listdir(data_path):
        if file_name.endswith(".pdf"):
            print(f"📄 Loading: {file_name}")
            loader = PyPDFLoader(os.path.join(data_path,file_name))
            docs = loader.load()
            all_docs.extend(docs)
    print(f"✅ Total documents loaded: {len(all_docs)}")

    return all_docs

def create_vector_store(docs):
    print("🔍 Splitting documents into chunks...")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)
    print(f"📦 Total chunks: {len(chunks)}")

    if not chunks:
            raise ValueError("No document chunks found. Please check your input files.")
    

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("faiss_index")
    print("✅ Vector store saved to 'faiss_index/'")

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)


