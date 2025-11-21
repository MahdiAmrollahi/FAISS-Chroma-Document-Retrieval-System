import faiss
import numpy as np


def build_faiss_index(vectors, index_path="vector_index.faiss"):
    """Build a FAISS index from the provided vectors with normalized embeddings"""
    vectors = np.array(vectors).astype("float32")
    if vectors.size == 0:
        raise ValueError("Cannot build FAISS index with zero vectors.")

    # Normalize L2 for better similarity search
    faiss.normalize_L2(vectors)

    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)
    faiss.write_index(index, index_path)
    print(f"Built FAISS index with {len(vectors)} normalized vectors, saved to {index_path}")
    return index


def search_faiss(query_vector, index_path="vector_index.faiss", n_results=5):
    """Search in FAISS index with normalized query vector"""
    index = faiss.read_index(index_path)
    
    # Convert query vector to numpy array
    if not isinstance(query_vector, np.ndarray):
        query_vector = np.array(query_vector)
    query_vector = query_vector.astype("float32").reshape(1, -1)
    
    # Normalize L2 for better similarity search
    faiss.normalize_L2(query_vector)
    
    # Search
    distances, indices = index.search(query_vector, n_results)
    
    return {
        "indices": indices[0].tolist(),
        "distances": distances[0].tolist(),
    }


def print_faiss_results(results, chunks):
    """Print FAISS search results"""
    if not results["indices"]:
        print("No results found")
        return
    
    for i, (idx, dist) in enumerate(zip(results["indices"], results["distances"])):
        chunk = chunks[idx] if idx < len(chunks) else "N/A"
        print(f"\n--- Result {i+1} ---")
        print(f"Index: {idx}")
        print(f"Distance: {dist:.4f}")
        print(f"Text: {chunk[:200]}..." if len(chunk) > 200 else f"Text: {chunk}")

