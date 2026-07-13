# Telecom RAG Assistant

## Overview

Telecom RAG Assistant is a Retrieval-Augmented Generation (RAG) chatbot built to answer questions related to telecom technologies using a curated knowledge base of telecom documents.

The application retrieves the most relevant sections from the knowledge base using semantic search and provides them as context to a Large Language Model before generating a response. This helps produce answers that are grounded in the uploaded documents instead of relying only on the model's internal knowledge.

The application also displays the retrieved document chunks and source references so that users can verify where the information was obtained.

---

## Application Preview

### Home

<img width="1915" height="811" alt="image" src="https://github.com/user-attachments/assets/dcdb5b8f-7ac0-407d-ac55-696b80459e2e" />


### Generated Response

<img width="1917" height="895" alt="image" src="https://github.com/user-attachments/assets/835abc20-84c5-4d4f-b8c6-c60f09cc0095" />

<img width="1290" height="735" alt="image" src="https://github.com/user-attachments/assets/8fa8125e-98ed-4718-9336-bec5014180bd" />


### Search History

<img width="1067" height="385" alt="image" src="https://github.com/user-attachments/assets/2346ef5d-6af0-4150-a805-3695650da265" />

<img width="1913" height="331" alt="image" src="https://github.com/user-attachments/assets/f800c473-4038-410e-bd24-5776004436ed" />



---

## Features

- Semantic search over telecom documents
- Retrieval-Augmented Generation (RAG)
- ChromaDB vector database
- HuggingFace MiniLM embeddings
- Gemini API integration
- Source document references
- Retrieved document chunks
- Search history logging
- Streamlit interface
- API error handling and retry mechanism

---

## Technologies Used

Frontend

- Streamlit

Backend

- Python

Libraries

- LangChain
- ChromaDB
- HuggingFace Embeddings
- PyMuPDF
- pandas
- python-dotenv

Embedding Model

- sentence-transformers/all-MiniLM-L6-v2

LLM

- Gemini Flash

---

## How it Works

1. Telecom PDF documents are loaded from the knowledge base.
2. The documents are split into overlapping chunks.
3. Embeddings are generated for every chunk using MiniLM.
4. The embeddings are stored in ChromaDB.
5. When the user asks a question, the question is embedded using the same embedding model.
6. ChromaDB retrieves the most relevant chunks.
7. The retrieved context is included in a prompt and sent to Gemini.
8. The generated response is displayed along with the retrieved sources and document chunks.

---

## Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Install the required packages

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=your_api_key
```

Generate the vector database

```bash
cd src
python embeddings.py
```

Run the Streamlit application

```bash
streamlit run Chat.py
```

---

## Sample Questions

- What is AMF?
- Explain Massive MIMO.
- What is O-RAN?
- What is Network Slicing?
- Explain the difference between AMF and SMF.
- What is RRC_INACTIVE?

---

## Search History

Every search is logged with the following information:

- Timestamp
- User question
- Generated response
- Source documents

The history can be viewed from the Search History page in the application.

---

## Knowledge Base

The chatbot uses a curated telecom knowledge base consisting of telecom standards and related documentation.

I intentionally did not provide an option for end users to upload documents through the interface. Since the application is designed to answer questions from trusted telecom documents, allowing unrestricted uploads could introduce irrelevant content into the vector database and negatively affect retrieval quality. Knowledge base updates are therefore performed offline by the administrator.

---

## Future Improvements

Some possible extensions for the project are:

- Support for multiple embedding models
- Hybrid keyword and semantic retrieval
- Authentication for administrator-only knowledge base updates
- Docker deployment
- Cloud deployment

---
