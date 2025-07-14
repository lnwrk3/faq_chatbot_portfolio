
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from app.vector_store import load_vector_store

def get_chain():
    vectordb = load_vector_store()
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    return qa_chain
