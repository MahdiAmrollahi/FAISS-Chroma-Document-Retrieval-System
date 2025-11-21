from sentence_transformers import SentenceTransformer
from vector_db_tools.basic import load_files, chunk_text
from vector_db_tools.chromadb_store import store_chunks_in_chromadb
from vector_db_tools.faiss_store import build_faiss_index


def main():
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    texts = load_files("data")
    nodes, metadata_list = chunk_text(texts)
    vectors = model.encode(nodes)

    build_faiss_index(vectors)
    store_chunks_in_chromadb(nodes, vectors, metadata_list)
    
    print(f"\n✓ Indexing complete!")
    print(f"  - FAISS index saved to: vector_index.faiss")
    print(f"  - ChromaDB collection saved to: ./chroma_db")


if __name__ == "__main__":
    main()