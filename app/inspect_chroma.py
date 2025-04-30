import os
import chromadb

# ─── Setup connection to ChromaDB ───
db_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
client = chromadb.PersistentClient(path=db_dir)

# ─── List all collections ───
collections = client.list_collections()
print("\n[Collections Found]:")
for coll in collections:
    print("-", coll.name)

# ─── Try to load the 'default' collection ───
try:
    collection = client.get_collection(name="unh_programs")
except Exception as e:
    print(f"Error loading collection: {e}")
    exit()

# ─── Check how many documents are inside ───
count = collection.count()
print(f"\n[Number of Documents]: {count}")

# ─── Preview some documents ───
if count > 0:
    docs = collection.peek()
    print("\n[Sample Documents]:")
    for doc in docs:
        print("-", doc)
else:
    print("\nNo documents found in 'default' collection.")

print("\n✅ Done inspecting ChromaDB.\n")
