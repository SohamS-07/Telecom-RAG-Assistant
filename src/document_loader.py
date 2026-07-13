import fitz
from pathlib import Path
from langchain_core.documents import Document

def extract_text(folder_path):
    documents=[]
    for pdf_file in Path(folder_path).glob("*.pdf"):
        doc=fitz.open(pdf_file)
        text=""
        for page in doc:
            text+=page.get_text()
        documents.append(Document(page_content=text,metadata={"source":pdf_file.name}))
    return documents
