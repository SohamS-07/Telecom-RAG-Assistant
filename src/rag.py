from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def similarity_search(question):
    embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vector_db=Chroma(persist_directory="chroma_db",embedding_function=embedding_model)
    docs=vector_db.similarity_search(query=question,k=5)
    return docs