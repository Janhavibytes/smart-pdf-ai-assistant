# 📄 Smart PDF AI Assistant

## 🚀 Overview

Smart PDF AI Assistant is a document-based question answering system that allows users to upload PDFs and interact with them through a chat interface.

It uses a **Retrieval-Augmented Generation (RAG)** approach to extract relevant content from documents and provide accurate responses without relying on external APIs.

---

## ✨ Features

* Upload and process multiple PDF files
* Chat-based interface for asking questions
* Fast semantic search using vector embeddings
* Clean and structured responses
* Source-aware retrieval system
* No external API dependency

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* PyPDF

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/smart-pdf-ai-assistant.git
cd smart-pdf-ai-assistant
```

### 2. Create virtual environment

```
python -m venv .venv
```

Activate:

```
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```
pip install streamlit langchain langchain-community langchain-text-splitters faiss-cpu pypdf sentence-transformers
```

### 4. Run the application

```
streamlit run app.py
```

---

## 🧠 How It Works

1. PDFs are uploaded and processed
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User query retrieves most relevant chunks
6. Answer is generated from retrieved content

---

## 📸 Demo

(Add a screenshot here before submission)

---

## 📌 Future Improvements

* Highlight answers inside PDF
* Voice-based interaction
* Multi-language support
* UI enhancements

---

## 👩‍💻 Author

Janhavi Rathod
