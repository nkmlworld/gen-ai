# build_index.py

from vector_store import load_docs, create_vector_store

docs = load_docs("data")
create_vector_store(docs)
print("✅ FAISS index created and saved at faiss_index/")
