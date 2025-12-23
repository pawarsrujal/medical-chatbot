# 🏥 Medical RAG Chatbot

A **Medical Question Answering Chatbot** built using **Retrieval-Augmented Generation (RAG)**.  
The chatbot retrieves relevant information from **medical PDF documents** stored in a **Pinecone vector database** and generates answers using a **Groq LLM**.

---

## 🚀 Project Overview

This project implements an AI-powered medical chatbot that:
- Loads medical PDFs
- Converts them into embeddings
- Stores them in Pinecone
- Retrieves relevant context for user questions
- Generates accurate answers using a Large Language Model

---

## 🧠 Tech Stack

- **Python 3.11**
- **Flask** – Backend web framework
- **LangChain** – RAG orchestration
- **Pinecone** – Vector database
- **Groq API** – LLM inference
- **Sentence Transformers** – Embeddings
- **PyPDF** – PDF text extraction
- **HTML / CSS / JavaScript** – Frontend UI

---

## ✨ Features

- 📄 PDF-based medical knowledge ingestion  
- 🔎 Semantic search using vector embeddings  
- 🧠 Fast LLM responses via Groq  
- ⚡ Real-time chatbot interaction  
- 🌐 Clean and responsive UI  
- 🔐 Secure environment variable usage  

---

## 📋 Prerequisites

- Python **3.11**
- Git
- Pinecone API key
- Groq API key

---


## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pawarsrujal/medical-chatbot.git
cd medical-chatbot
```

### 2. Create Virtual Environment

Create a Python 3.11 virtual environment named `chat`:

```powershell
# Windows PowerShell
py -3.11 -m venv chat
```

```bash
# Linux/Mac
python3.11 -m venv chat
```

### 3. Activate Virtual Environment

```powershell
# Windows PowerShell
.\chat\Scripts\Activate.ps1
```

```bash
# Linux/Mac
source chat/bin/activate
```

**Note**: If you encounter an execution policy error on Windows, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
pip install groq
```


This will install all required packages including:
- LangChain (0.3.26) - AI framework
- Flask (3.1.1) - Web framework
- Sentence Transformers (4.1.0) - Embeddings
- PyPDF (5.6.1) - PDF processing
- Pinecone - Vector database
- Groq - LLM integration

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
```

## 📁 Project Structure

```
medical-chatbot/
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup configuration
├── .env                        # Environment variables (not tracked in git)
├── chat/                       # Virtual environment directory
├── src/
│   ├── __init__.py
│   ├── helper.py              # Helper functions
│   └── prompt.py              # Prompt templates
├── research/
│   └── trials.ipynb           # Jupyter notebook for experiments
├── README.md                  # Project documentation
└── LICENSE                    # License file
```

## 🎯 Features

- **Medical Query Processing**: Answer medical questions using AI
- **Vector Database Integration**: Efficient similarity search with Pinecone
- **PDF Document Processing**: Extract and process medical documents
- **Web Interface**: Flask-based web application
- **Embeddings**: Sentence transformers for semantic search

## 💻 Usage

### Run the Application

```bash
python app.py
```

The Flask server will start and you can access the chatbot interface.

## 🔧 Development

### Package Information

- **Name**: medical-chatbot
- **Version**: 0.1.0
- **Author**: Srujal Pawar
- **Email**: srujalpawar2004@gmail.com

### 🔑 Key Dependencies

| Package | Version | Purpose |
|-------|--------|--------|
| flask | 3.1.1 | Web framework for chatbot UI |
| langchain | 0.3.26 | RAG orchestration framework |
| langchain-community | 0.3.26 | Document loaders & utilities |
| langchain-pinecone | 0.2.8 | Pinecone vector store integration |
| sentence-transformers | 4.1.0 | Text embedding generation |
| pypdf | 5.6.1 | PDF document processing |
| pinecone-client | latest | Vector database backend |
| groq | latest | LLM inference (LLaMA 3.1) |
| python-dotenv | 1.1.0 | Environment variable management |
| requests | latest | API communication |


## 📝 License

This project is licensed under the terms specified in the LICENSE file.

## 👨‍💻 Author

**Srujal Pawar**
- GitHub: [@pawarsrujal](https://github.com/pawarsrujal)
- Email: srujalpawar2004@gmail.com

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

For support, email srujalpawar2004@gmail.com or open an issue in the repository.

---

**Note**: Make sure to keep your API keys secure and never commit them to version control. The `.env` file should be added to `.gitignore`.
