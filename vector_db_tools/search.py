from .faiss_store import print_faiss_results, search_faiss
from .chromadb_store import print_search_results, search_chromadb


def search(query_vector, chunks=None, backend="both", n_results=5, 
           faiss_index_path="vector_index.faiss",
           chromadb_collection="documents",
           chromadb_path="./chroma_db"):
    """
    Unified search function that supports both FAISS and ChromaDB
    
    Args:
        query_vector: Query embedding vector (only thing needed for search)
        chunks: Optional list of text chunks (only used for displaying FAISS results text)
        backend: "faiss", "chromadb", or "both"
        n_results: Number of results to return
        faiss_index_path: Path to FAISS index file
        chromadb_collection: ChromaDB collection name
        chromadb_path: Path to ChromaDB database
    
    Returns:
        Dictionary with search results from selected backend(s)
    """
    results = {}
    
    if backend in ["faiss", "both"]:
        # FAISS search only needs query_vector - it searches embeddings
        faiss_results = search_faiss(query_vector, faiss_index_path, n_results)
        results["faiss"] = faiss_results
        
        # chunks only used for displaying result texts (FAISS returns indices, not texts)
        if chunks:
            print("\n=== FAISS Results ===")
            print_faiss_results(faiss_results, chunks)
        else:
            print("\n=== FAISS Results ===")
            print("(chunks not provided - showing indices only)")
            for i, (idx, dist) in enumerate(zip(faiss_results["indices"], faiss_results["distances"])):
                print(f"Result {i+1}: Index={idx}, Distance={dist:.4f}")
    
    if backend in ["chromadb", "both"]:
        chromadb_results = search_chromadb(
            query_vector, 
            chromadb_collection, 
            n_results, 
            chromadb_path
        )
        results["chromadb"] = chromadb_results
        
        print("\n=== ChromaDB Results ===")
        print_search_results(chromadb_results)
    
    return results


def search_text(query_text, model, chunks=None, backend="both", n_results=5,
                faiss_index_path="vector_index.faiss",
                chromadb_collection="documents",
                chromadb_path="./chroma_db"):
    """
    Search using text query (automatically encodes the query)
    
    Args:
        query_text: Text query string
        model: SentenceTransformer model for encoding
        chunks: Optional list of text chunks (only needed to display FAISS result texts)
        backend: "faiss", "chromadb", or "both"
        n_results: Number of results to return
        faiss_index_path: Path to FAISS index file
        chromadb_collection: ChromaDB collection name
        chromadb_path: Path to ChromaDB database
    
    Returns:
        Dictionary with search results from selected backend(s)
    """
    query_vector = model.encode([query_text])[0]
    print(f"\nSearching for: '{query_text}'")
    return search(
        query_vector, 
        chunks, 
        backend, 
        n_results,
        faiss_index_path,
        chromadb_collection,
        chromadb_path
    )

