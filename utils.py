from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents_with_metadata(file_path):
    """
    Loads a document and assigns the file name as source metadata.
    """
    # Get the file extension to determine the loader
    _, extension = os.path.splitext(file_path)
    
    if extension.lower() == ".pdf":
        loader = PyPDFLoader(file_path)
    elif extension.lower() == ".docx":
        loader = UnstructuredWordDocumentLoader(file_path)
    else:
        print(f"Unsupported file type: {extension}. Skipping.")
        return []

    # Load the document
    docs = loader.load()
    
    # Attach the source file name to each document's metadata
    for doc in docs:
        doc.metadata["source"] = os.path.basename(file_path)
        
    return docs

def process_and_chunk_documents(folder_path):
    """
    Loads all supported documents from a folder, processes them, 
    and splits them into chunks for embedding.
    """
    all_docs = []
    # List all files in the given folder path
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Ensure it is a file before processing
        if os.path.isfile(file_path):
            docs = load_documents_with_metadata(file_path)
            all_docs.extend(docs)

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    
    # Split the documents into chunks
    chunked_docs = text_splitter.split_documents(all_docs)
    
    print(f"Successfully loaded and chunked {len(chunked_docs)} documents from the '{folder_path}' folder.")
    return chunked_docs