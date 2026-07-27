import os 
import tempfile
from pathlib import Path
from langchain_community.document_loaders import  (
    TextLoader , PyPDFLoader
)
def load_txt():
    with tempfile.NamedTemporaryFile(delete=False , suffix=".txt") as temp_file:
        temp_file.write(b"Hello world ")
        temp_file_path = temp_file.name
        
    try:
        
        loader = TextLoader(temp_file_path)
        documents = loader.load()
        
    
        
        for doc in documents:
            print(doc.page_content)
            print()
            
    finally:
        os.remove(temp_file_path)
        
def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    print( f"Loaded {len(documents)} document(s) from PDF")
    for i, doc in enumerate(documents):
        print(f"Document {i+1} Content Preview: {doc.page_content [ : 1]}")
        print( f"Metadata: {doc.metadata}")
        
if __name__ == "__main__":
    load_pdf("C:/Users/HP/Downloads/Strategic Scaling_ Production RAG Platform Blueprint - Google Docs.pdf")
 