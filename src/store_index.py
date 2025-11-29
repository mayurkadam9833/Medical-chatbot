from langchain.vectorstores import Chroma 
from src.helper import text_splitter,load_pdf_files,download_embeddings 



extracted_data=load_pdf_files("Data/")
text_chunk=text_splitter(extracted_data)
embeddings=download_embeddings()

dir="vector_database/"

vector_database=Chroma.from_documents(
    documents=text_chunk, 
    persist_directory=dir, 
    embedding=embeddings
)