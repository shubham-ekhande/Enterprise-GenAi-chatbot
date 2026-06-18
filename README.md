Enterprise GenAI Chatbot

An AI-powered Enterprise Knowledge Assistant built using LangChain, ChromaDB, Ollama, and Streamlit. 
The chatbot enables users to interact with enterprise documents through natural language queries using Retrieval-Augmented Generation (RAG).

Features
PDF document ingestion and processing
Semantic search using vector embeddings
Retrieval-Augmented Generation (RAG)
Conversational memory support
Enterprise knowledge base querying
Local LLM integration using Ollama
Interactive Streamlit web interface
Chat analytics and logging dashboard
Tech Stack
Frontend
Streamlit
Backend
Python
LangChain
AI & NLP
Ollama
Llama 3.2 / CodeLlama
Sentence Transformers
Vector Database
ChromaDB
Document Processing
PyPDF
Project Structure

enterprise-genai-chatbot/

├── analytics/

├── chatbot/

├── data/

├── enterprise_pdf_generator/

├── uploaded_pdfs/

├── app.py

├── dashboard.py

├── requirements.txt

└── .gitignore

How It Works
Upload enterprise PDF documents.
Documents are split into smaller chunks.
Text embeddings are generated using Sentence Transformers.
Embeddings are stored in ChromaDB.
User queries are converted into embeddings.
Relevant document chunks are retrieved.
Retrieved context is passed to the LLM.
The model generates accurate responses based on enterprise documents.
Installation
Clone Repository

git clone https://github.com/shubham-ekhande/enterprise-genai-chatbot.git

cd enterprise-genai-chatbot

Create Virtual Environment

python -m venv venv

Activate Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Install Ollama

Download and install Ollama.

Pull a model:

ollama pull llama3.2:1b

or

ollama pull codellama

Run Application

streamlit run app.py

Future Enhancements
Voice-enabled interactions
Multi-document collections
User authentication
Role-based access control
Cloud deployment
Advanced analytics dashboard
