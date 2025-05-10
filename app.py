# app.py

import streamlit as st
from rag_chain import get_rag_chain
from agent import get_agent

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("📚 RAG-Based Chatbot")

# Load RAG chain and agent
rag_chain = get_rag_chain()
agent = get_agent()

# Streamed chat UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.chat_input("Ask a question based on the documents:")

if user_query:
    st.session_state.chat_history.append(("user", user_query))
    with st.spinner("Thinking..."):
        response = agent.run(user_query)
        final_answer = response.content 
        st.session_state.chat_history.append(("assistant", final_answer))

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)
