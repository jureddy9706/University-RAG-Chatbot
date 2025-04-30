from sentence_transformers import SentenceTransformer
import chromadb
import os

# Setup
db_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
client = chromadb.PersistentClient(path=db_dir)
collection = client.get_collection(name="default")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Try a manual query
query = "master's in data science"
query_embedding = embedding_model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    include=["documents"]
)

print(results)
