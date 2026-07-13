from document_loader import extract_text
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking_return():
    documents=extract_text("C:/Users/Soham Sood/Internship_Amantya/Week6/knowledge_base")
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=125,length_function=len,is_separator_regex=False)
    texts=text_splitter.split_documents(documents)
    return texts