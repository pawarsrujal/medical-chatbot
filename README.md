# Medical Chatbot

A medical chatbot application built with LangChain, Flask, and Pinecone vector database for intelligent medical query responses.

## 🚀 Project Overview

This project implements an AI-powered medical chatbot that can answer medical queries using advanced natural language processing and retrieval-augmented generation (RAG) techniques.

## 📋 Prerequisites

- Python 3.11
- Git

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
```

This will install all required packages including:
- LangChain (0.3.26) - AI framework
- Flask (3.1.1) - Web framework
- Sentence Transformers (4.1.0) - Embeddings
- PyPDF (5.6.1) - PDF processing
- Pinecone - Vector database
- OpenAI - LLM integration

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
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

### Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| langchain | 0.3.26 | AI/LLM framework |
| langchain-openai | 0.3.24 | OpenAI integration |
| langchain-pinecone | 0.2.8 | Pinecone vector store |
| langchain-community | 0.3.26 | Community integrations |
| flask | 3.1.1 | Web framework |
| sentence-transformers | 4.1.0 | Text embeddings |
| pypdf | 5.6.1 | PDF processing |
| python-dotenv | 1.1.0 | Environment management |

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