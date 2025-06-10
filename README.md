# UNH RAG Chatbot – AI Assistant for University of New Haven  -- http://44.217.147.240:8000

![Status](https://img.shields.io/badge/status-production-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

This is a production-grade, GPU-accelerated **Retrieval-Augmented Generation (RAG) chatbot** that answers queries about the University of New Haven using scraped web data. It uses **ChromaDB**, **Ollama LLM**, and **Apache Airflow** for automation, with deployment on **AWS EC2 (GPU)**.

---

## 🚀 Features

- 🔍 Scrapes university content using sitemap filtering
- 🧠 Embeds documents into ChromaDB with `all-MiniLM-L6-v2` 
- 💬Interactive Chat Interface – Simple and user-friendly web-based chatbot
- 🔍Vector Search with ChromaDB – Efficient information retrieval for precise answers
- 💬 Uses **Ollama Mistral 7B** (LLM) for fast, high-quality answers
- 🧩 Chunked input for semantic search (chunk size = 500, overlap = 100)
- ⚙️ Airflow DAG automates monthly refresh of documents
- 🎛️ Configurable via `config.yaml` (no code changes needed)
- 🔴Real-time Updates – Continuously learns from newly extracted data
- ☁️Deployment Ready – Can be hosted on cloud platforms



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
git clone
```bash
https://github.com/jureddy9706/UNH_CHATBOT.git
cd UNH_CHATBOT 
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Update config(optional)
If you're not using Airflow yet, you can directly edit config.yaml
Edit config.yaml to your desired setup:

```bash
model_name: "mistral"
embedding_model: "all-MiniLM-L6-v2"
chunk_size: 500
overlap: 100
sitemap_url: "https://university.edu/sitemap.xml"
```

### 4. Run chatbot locally
```bash
uvicorn app.chatbot_api:app --reload
```
### 5. Launch Airflow in a different terminal
```bash
airflow standalone
```
## 🧪 Example Chatbot Demo

User: Who is Sula?

Bot: Ardiana Sula is a recognized scholar and researcher with degrees from Harvard University Business School, University Polytechnic of Tirana, Fukuoka Institute of Technology, and Drexel University. She is a legislative intern with the Anti-Defamation League and focuses her research on emerging technologies and practices in real-time video classroom formats, educational designs, and globalized virtual

User: who is aminul?

Bot: Muhammad Aminul Islam is an Assistant Professor with the Department of Electrical and Computer Engineering and Computer Science at the University of New Haven, Connecticut, USA. His research interests include deep learning, computer vision, information fusion, autonomous driving, and remote sensing.

User: vahis?

Bot: Based on the provided context, 'vahis' is not mentioned. It seems there might be a typo or error in the question. If you meant 'Vahid Behzadan', that is the name of the assistant professor who was quoted in several media articles regarding cybersecurity, Al, and computers, as well as demand for laptops and tablets during the pandemic, and concerns about emails being written by an artificial intelligence

User: vahid?

Bot: Vahid Behzadan is an assistant professor who specializes in various fields including electrical and computer engineering, computer science, cybersecurity, networks, data science. He has directed the Secure and Assured Intelligent Learning (SAIL) Lab and has commented on issues related to Venmo app security, increase in cyber-attacks during the Coronavirus lockdown, ransomware, Zoom security risks for the Department of Defense, cybersecurity, Al, cryptocurrency origins, computer hacking, the recent targets and frequency of ransomware attacks, and possible security issues for users of Amazon Sidewalk.

## ☁️ EC2 Deployment (Optional)

1. Launch EC2 (Ubuntu with GPU)
2. SSH into instance
3. Install Python 3.10+, Ollama, and system packages
4. Clone repo, install dependencies
5. Start chatbot with:
```bash
uvicorn app.chatbot_api:app --host 0.0.0.0 --port 8000
```
6. Access from browser: http://<ec2-public-ip>:8000

## 🔧 Customization

You can build a chatbot for any college by changing just the sitemap URL and parameters in config.yaml or in airflow. No code changes required!

## 📜 License

MIT License. This project is for academic and educational purposes.

