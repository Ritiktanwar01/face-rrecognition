import chromadb
from chromadb.config import Settings

# Initialize local client (default stores in ~/.chromadb)
client = chromadb.Client(Settings())

# Create or get collection
collection = client.get_or_create_collection(name="faces")

# ---------- CREATE ----------
def add_face_embedding(face_id: str, embedding: list[float], metadata: dict):
    """
    Add a new facial embedding to the collection.
    Args:
        face_id: Unique ID for the person (e.g., "person1")
        embedding: List of floats (the facial embedding vector)
        metadata: Dictionary with extra info (e.g., {"name": "Alice"})
    """
    collection.add(ids=[face_id], embeddings=[embedding], metadatas=[metadata])
    return f"Added embedding for {face_id}"

# ---------- READ ----------
def get_face_embedding(face_id: str):
    """
    Retrieve embedding + metadata by ID.
    """
    result = collection.get(ids=[face_id])
    return result

def search_similar_faces(query_embedding: list[float], top_k: int = 3):
    """
    Find most similar faces to a given embedding.
    """
    result = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return result

# ---------- UPDATE ----------
def update_face_embedding(face_id: str, new_embedding: list[float], new_metadata: dict):
    """
    Update an existing embedding by re‑adding with same ID.
    """
    collection.update(ids=[face_id], embeddings=[new_embedding], metadatas=[new_metadata])
    return f"Updated embedding for {face_id}"

# ---------- DELETE ----------
def delete_face_embedding(face_id: str):
    """
    Delete embedding by ID.
    """
    collection.delete(ids=[face_id])
    return f"Deleted embedding for {face_id}"
