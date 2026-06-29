# RAG PDF Chatbot

A chatbot that lets you upload any PDF and ask questions about it. Instead of reading through the whole document, you can ask what you 
want to know and get a direct answer based on the document content.

## What it does

The app takes a PDF, breaks it into small chunks, converts them into vectors, and stores them locally. When a question is asked, it finds 
the most relevant chunks and sends them to Claude AI which then answers based only on what is in the document.

## About this project

This project demonstrates how RAG works in a practical use case. It was tested with the "Attention Is All You Need" paper, the research 
paper that introduced the Transformer architecture behind modern AI models like ChatGPT and Claude.

## Tech Stack

- LangChain for the RAG pipeline
- ChromaDB as the vector store
- Anthropic Claude API as the language model
- HuggingFace Sentence Transformers for embeddings
- Streamlit for the web interface
- PyPDF for reading PDF files


## Sample results

See demo_results.txt for sample questions and answers about the Attention paper, including questions about the Transformer architecture, 
attention mechanisms, and model performance.
