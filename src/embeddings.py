from chunking import chunking_return
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def embedding_return():
    embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vector_db=Chroma(persist_directory="chroma_db",embedding_function=embedding_model)
    vector_db.reset_collection()
    chunks=chunking_return()
    vector_db.add_documents(chunks)
    print("Total chunks stored:", vector_db._collection.count())
    print(f"Added {len(chunks)} chunks into ChromaDB")
    return vector_db
if __name__ == "__main__":
    embedding_return()

