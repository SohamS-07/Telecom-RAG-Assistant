import streamlit as st
from llm import generate_response
from log import log_query

st.set_page_config(page_title='Telecom RAG Assistant')
st.title("Telecom RAG Assistant")
question=st.text_input("Ask a telecom question")
if st.button("Ask"):
    with st.spinner("Searching Database"):
        answer,docs=generate_response(question)
        log_query(question,answer,docs)
    st.write(answer)
    st.subheader('Sources')
    sources=sorted({doc.metadata["source"] for doc in docs})
    for source in sources:
        st.write(f"-{source}")
    st.subheader("Retrieved Context")
    for i,doc in enumerate(docs,start=1):
        with st.expander(f"chunk {i}"):
            st.write(doc.page_content)