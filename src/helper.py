from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.embeddings import HuggingFaceEmbeddings 


def load_pdf_files(data): 
    loader=DirectoryLoader(
        data, 
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents 


def text_splitter(data): 
    text_split=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunk=text_split.split_documents(data)
    return text_chunk

def download_embeddings(): 
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")