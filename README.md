# RAG-PDF-Chatbot

# 📄 RAG PDF Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload any PDF and ask questions about its content using Claude AI.

## 🚀 Demo

Tested with the "Attention Is All You Need" paper — the foundational Transformer architecture paper that powers modern AI models like ChatGPT and Claude.

## 🛠️ Tech Stack

- LangChain — RAG pipeline framework
- ChromaDB — Vector store for document embeddings
- Anthropic Claude API — LLM for generating answers
- HuggingFace Embeddings — Converting text to vectors
- Streamlit — Web UI
- PyPDF — PDF loading

## How It Works

1. Upload any PDF document
2. Document is split into chunks of 500 characters
3. Each chunk is converted to vectors (embeddings)
4. Vectors are stored in ChromaDB locally
5. User asks a question
6. System finds the 3 most relevant chunks
7. Claude AI answers based only on those chunks

## Setup

1. Clone the repository
2. Create a .env file with your API key:
ANTHROPIC_API_KEY=your-api-key-here
3. Install requirements:
pip install langchain langchain-anthropic langchain-community langchain-text-splitters chromadb pypdf streamlit python-dotenv sentence-transformers
4. Run the app:
streamlit run app.py

## Demo Results

See demo_results.txt for sample Q&A results from the Attention Is All You Need paper.
