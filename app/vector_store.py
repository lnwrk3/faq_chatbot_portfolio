from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.loaders import load_faq_csv

def build_vector_store(csv_path: str, persist_path: str = "faiss_index") -> FAISS:
    docs = load_faq_csv(csv_path)
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local(persist_path)
    return vector_store

def load_vector_store(persist_path: str = "faiss_index") -> FAISS:
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)
