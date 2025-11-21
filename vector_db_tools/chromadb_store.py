import chromadb
import numpy as np


def store_chunks_in_chromadb(chunks, vectors, metadata_list=None, collection_name="documents", path="./chroma_db"):
    """Store chunks and vectors in ChromaDB with normalized embeddings"""
    client = chromadb.PersistentClient(path=path)
    
    # Convert vectors to numpy array and normalize
    if isinstance(vectors, np.ndarray):
        vectors = vectors.astype("float32")
    else:
        vectors = np.array(vectors).astype("float32")
    
    # Normalize L2 for better similarity search
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    vectors = vectors / (norms + 1e-8)  # Add small epsilon to avoid division by zero
    
    # Convert to list
    vectors_list = [v.tolist() for v in vectors]
    
    # Delete existing collection if it exists
    try:
        client.delete_collection(name=collection_name)
    except:
        pass
    
    # Create new collection
    collection = client.create_collection(name=collection_name)
    
    # Add data with metadata
    for i, (chunk, vector) in enumerate(zip(chunks, vectors_list)):
        # Use metadata if provided, otherwise use default
        if metadata_list and i < len(metadata_list):
            meta = metadata_list[i].copy()
            meta["chunk_id"] = i
        else:
            meta = {"source": f"chunk_{i}", "chunk_id": i}
        
        # Use source filename or chunk_id as part of the ID
        source = meta.get("source", f"chunk_{i}")
        emb_id = f"{source}_{i}"
        
        collection.add(
            documents=[chunk],
            metadatas=[meta],
            ids=[emb_id],
            embeddings=[vector],
        )
    
    print(f"Stored {len(chunks)} chunks in ChromaDB (with normalized embeddings)")
    return collection


def search_chromadb(query_vector, collection_name="documents", n_results=5, path="./chroma_db"):
    """Search in ChromaDB with normalized query vector"""
    client = chromadb.PersistentClient(path=path)
    collection = client.get_collection(name=collection_name)
    
    # Convert to numpy array and normalize
    if isinstance(query_vector, np.ndarray):
        query_vector = query_vector.astype("float32")
    else:
        query_vector = np.array(query_vector).astype("float32")
    
    # Normalize L2 for better similarity search
    norm = np.linalg.norm(query_vector)
    if norm > 0:
        query_vector = query_vector / norm
    
    # Convert to list
    query_vector = query_vector.tolist()
    
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )
    
    return results


def print_search_results(results):
    """Print search results"""
    if not results["documents"] or not results["documents"][0]:
        print("No results found")
        return
    
    for i, (doc, meta, dist) in enumerate(
        zip(results["documents"][0], results["metadatas"][0], results["distances"][0])
    ):
        print(f"\n--- Result {i+1} ---")
        print(f"Distance: {dist:.4f}")
        print(f"Source: {meta.get('source', 'N/A')}")
        print(f"Text: {doc[:200]}..." if len(doc) > 200 else f"Text: {doc}")
