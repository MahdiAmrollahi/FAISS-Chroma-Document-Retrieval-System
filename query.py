import sys
from sentence_transformers import SentenceTransformer
from vector_db_tools.search import search_text
from vector_db_tools.basic import load_files, chunk_text

def main():
    # Load the same model used for indexing
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    
    # Get query from command line or use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "Why Python"
        print("No query provided, using default query")
    nodes, _ = chunk_text(load_files("data"))

    # Search in both FAISS and ChromaDB
    # Note: chunks parameter is optional - only needed to display FAISS result texts
    # ChromaDB will show texts automatically
    search_text(query, model, nodes, backend="both", n_results=5)
    
    # You can also search in specific backend:
    # search_text(query, model, backend="faiss", n_results=5)
    # search_text(query, model, backend="chromadb", n_results=5)


if __name__ == "__main__":
    main()

