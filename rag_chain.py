# rag_chain.py

from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from vector_store import load_vector_store
# from utils import get_llm


def get_rag_chain():
    # Load Hugging Face model and tokenizer
    llm = get_llm()
    prompt_template = PromptTemplate(
                    input_variables=["context", "question"],
                    template="""
            Use the context below to answer the question as accurately as possible.
            Do not assume the answer if not sure, respond with
            "Sorry, not sure"
            Context:
            {context}

            Question:
            {question}

            Answer:
            """
                )

    # Load retriever
    vectorstore = load_vector_store()
    retriever = vectorstore.as_retriever(search_type="similarity", k=10)

    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt_template)

    # Create RAG chain
    rag_chain = RetrievalQA(combine_documents_chain=chain, retriever=retriever, return_source_documents=True)

    return rag_chain
