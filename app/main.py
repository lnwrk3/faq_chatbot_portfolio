
import streamlit as st
from app.chains import get_chain

st.set_page_config(page_title="社内FAQチャットボット", page_icon="🤖")
st.title("📚 社内FAQチャットボット")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

qa_chain = get_chain()

def format_sources(sources):
    return "\n".join([f"- {doc.metadata['source']}" for doc in sources])

user_input = st.chat_input("質問をどうぞ")
if user_input:
    with st.spinner("考え中..."):
        result = qa_chain({"question": user_input, "chat_history": st.session_state.chat_history})
        answer = result["answer"]
        sources = format_sources(result["source_documents"])
        st.session_state.chat_history.append((user_input, answer + "\n\n📎 参照元:\n" + sources))

for i, (q, a) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)
