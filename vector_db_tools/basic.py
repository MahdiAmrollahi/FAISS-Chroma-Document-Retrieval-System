from pathlib import Path
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter


def load_files(folder_path):
    documents = SimpleDirectoryReader(input_dir=folder_path).load_data()
    return documents


def chunk_text(documents):
    parser = SentenceSplitter(chunk_size=128, chunk_overlap=32)
    nodes = parser.get_nodes_from_documents(documents)
    
    chunks = []
    metadata_list = []
    
    for node in nodes:
        chunks.append(node.text)
        
        # Extract metadata from node
        meta = node.metadata if hasattr(node, 'metadata') else {}
        file_path = meta.get('file_path', meta.get('file_name', 'unknown'))
        filename = Path(file_path).name if file_path != 'unknown' else 'unknown'
        
        metadata_list.append({
            "source": filename,
            "file_path": file_path,
            "chunk_index": len(chunks) - 1
        })
    
    return chunks, metadata_list