# UNH Chatbot – AI Assistant for University of New Haven

This project is a production-grade, GPU-accelerated **RAG (Retrieval-Augmented Generation) chatbot** built to answer questions related to the University of New Haven. It uses a combination of **ChromaDB**, **Ollama LLM**, **Hugging Face embeddings**, and **Airflow** for automation.

---

## 🚀 Features

- 🔍 Scrapes and filters university content via sitemap XML
- 🧠 Vector-based document retrieval using ChromaDB
- 💬 Natural language answers using Ollama Mistral 7B (on GPU)
- 📊 Auto-chunking of content with overlap for semantic accuracy
- 📅 Monthly data refresh using Apache Airflow DAGs
- 🔧 Parameterized automation: update URL, model, chunk size dynamically

---

## 🧠 Tech Stack

- **Language Model**: [Ollama Mistral 7B](https://ollama.com/library/mistral)
- **Embedding Model**: `all-MiniLM-L6-v2` from Hugging Face
- **Vector Store**: ChromaDB
- **Scheduler**: Apache Airflow
- **Web Server**: FastAPI
- **Cloud**: AWS EC2 (Ubuntu with GPU)

---

## 📁 Project Structure
UNH_CHATBOT/ ├── app/ # Core chatbot logic and processing │ ├── chatbot_api.py │ ├── embed_documents.py │ ├── evaluate_metrics.py │ ├── scrape_website.py │ └── ... ├── airflow/ # Airflow DAGs for automation │ └── college_rag_update_dag.py ├── cleaned_texts/ # Cleaned HTML/text from sitemap ├── chroma_db/ # Vector DB (excluded from Git) ├── templates/ # Frontend templates (HTML) ├── static/ # CSS / assets ├── logs/ # App and pipeline logs ├── .gitignore └── README.md


---

## 📡 Data Pipeline Summary

1. **Scraping**: Extracts pages from the sitemap URL  
   - Filters: `admissions`, `tuition fees`, `programs`, `student life`, `housing`, `scholarships`, `alumni`, `jobs`, etc.  
   - Blocks: `news`, `blogs`, `events`, `newsletter`, etc.

2. **Cleaning**: Text is cleaned and stored in `cleaned_texts/`

3. **Embedding**: Text is chunked (size=500, overlap=100), embedded using `all-MiniLM-L6-v2`, and stored in ChromaDB

4. **Chatbot Logic**:  
   - User asks question  
   - Relevant context retrieved from ChromaDB  
   - Combined context + question sent to **Ollama Mistral 7B**  
   - Answer is generated and displayed in under 5 seconds

5. **Automation**:  
   - Airflow DAG (`college_rag_update_dag.py`) runs on the 1st of every month  
   - DAG can be triggered manually with updated parameters:
     - Embedding model
     - Chunk size
     - LLM model
     - College sitemap URL

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/jureddy9706/UNH_CHATBOT.git
   cd UNH_CHATBOT

