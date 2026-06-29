from rag import load_pdf, create_vectorstore, create_chain
from datetime import datetime

# Path to your PDF
PDF_PATH = r"C:\Users\tourl\OneDrive\Υπολογιστής\2026 Portfolio Projects\Rag-PDF-Chatbot\attention_paper.pdf"

# The 5 questions
QUESTIONS = [
    "What is the Transformer architecture and what problem does it solve?",
    "How does scaled dot-product attention work?",
    "What is the difference between self-attention and multi-head attention?",
    "Why is the Transformer faster to train than RNN models?",
    "What were the main results of the paper and what BLEU score was achieved?"
]

def run_demo():
    print("=" * 60)
    print("RAG PDF Chatbot - Demo Results")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    print("\nLoading PDF...")
    pages = load_pdf(PDF_PATH)
    print("Creating vector store...")
    vectorstore = create_vectorstore(pages)
    print("Creating chain...")
    chain = create_chain(vectorstore)
    print("\nReady! Running questions...\n")
    
    with open("demo_results.txt", "w", encoding="utf-8") as f:
        f.write("RAG PDF Chatbot - Demo Results\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("=" * 60 + "\n\n")
        
        for i, question in enumerate(QUESTIONS, 1):
            print(f"Question {i}: {question}")
            print("-" * 40)
            
            answer = chain.invoke(question)
            
            print(f"Answer: {answer}")
            print()
            
            f.write(f"Question {i}: {question}\n")
            f.write(f"Answer: {answer}\n")
            f.write("-" * 60 + "\n\n")
    
    print("=" * 60)
    print("Done! Results saved to demo_results.txt")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()