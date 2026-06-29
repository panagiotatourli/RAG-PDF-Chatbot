import streamlit as st
from rag import load_pdf, create_vectorstore, create_chain
import tempfile
import os

st.title("📄 Chat with your PDF")
st.write("Upload a PDF and ask questions about it!")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Reading your PDF..."):
        pages = load_pdf(tmp_path)
        vectorstore = create_vectorstore(pages)
        chain = create_chain(vectorstore)
    
    st.success("PDF loaded! Ask me anything!")

    question = st.text_input("Your question:")
    
    if question:
        with st.spinner("Thinking..."):
            answer = chain.invoke(question)
            st.write("**Answer:**", answer)
    
    os.unlink(tmp_path)