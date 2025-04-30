# UNH Chatbot – AI Assistant for University of New Haven

![Status](https://img.shields.io/badge/status-production-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

This is a production-grade, GPU-accelerated **Retrieval-Augmented Generation (RAG) chatbot** that answers queries about the University of New Haven using scraped web data. It uses **ChromaDB**, **Ollama LLM**, and **Apache Airflow** for automation, with deployment on **AWS EC2 (GPU)**.

---

## 🚀 Features

- 🔍 Scrapes university content using sitemap filtering
- 🧠 Embeds documents into ChromaDB with `all-MiniLM-L6-v2`
- 💬 Uses **Ollama Mistral 7B** (LLM) for fast, high-quality answers
- 🧩 Chunked input for semantic search (chunk size = 500, overlap = 100)
- ⚙️ Airflow DAG automates monthly refresh of documents
- 🎛️ Configurable via `config.yaml` (no code changes needed)

---

## 🧠 Tech Stack

- **LLM**: [Ollama Mistral 7B](https://ollama.com/library/mistral)
- **Embeddings**: Hugging Face `all-MiniLM-L6-v2`
- **Vector Store**: ChromaDB
- **Web API**: FastAPI
- **Scheduler**: Apache Airflow
- **Deployment**: AWS EC2 with GPU (Ubuntu)
- **Frontend**: HTML/CSS/JS with Bootstrap

---

## 📁 Project Structure

UNH_CHATBOT/
├── app/                     # Core chatbot logic and processing
│   ├── chatbot_api.py
│   ├── embed_documents.py
│   ├── evaluate_metrics.py
│   ├── scrape_website.py
│   └── ...
├── airflow/                 # Airflow DAGs for automation
│   └── college_rag_update_dag.py
├── cleaned_texts/           # Cleaned HTML/text from sitemap
├── chroma_db/               # Vector DB (excluded from Git)
├── templates/               # Frontend templates (HTML)
├── static/                  # CSS / assets
├── logs/                    # App and pipeline logs
├── config.yaml              # Configuration file for parameters
├── .gitignore
└── README.md

---

## 📡 Pipeline Summary

### 🔄 Data Flow:

1. **Scraping**  
   Uses sitemap `https://university.edu/sitemap.xml`  
   Filters: `admissions`, `international`, `tuition fees`, `programs`, `student life`, etc.  
   Blocks: `blogs`, `newsletters`, `events`, etc.

2. **Cleaning**  
   Removes HTML clutter → saves in `cleaned_texts/`

3. **Embedding**  
   Chunks text (size=500, overlap=100) and embeds using SentenceTransformers → stores in ChromaDB

4. **Chatbot Flow**
   - User submits query via FastAPI
   - Retrieves top relevant chunks from ChromaDB
   - Passes context + query to **Ollama Mistral 7B**
   - Returns answer in under 5 seconds

5. **Airflow Automation**  
   DAG scheduled for the 1st of each month to:
   - Rescrape site
   - Clean and re-embed data
   - Use `config.yaml` parameters (LLM model, chunk size, URL)

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone
1. https://github.com/jureddy9706/UNH_CHATBOT.git
cd UNH_CHATBOT 
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Update config
Edit config.yaml to your desired setup:

```bash
model_name: "mistral"
embedding_model: "all-MiniLM-L6-v2"
chunk_size: 500
overlap: 100
sitemap_url: "https://university.edu/sitemap.xml"
```

4. Run chatbot locally
```bash
uvicorn app.chatbot_api:app --reload
```

