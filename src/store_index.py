from dotenv import load_dotenv
import os
os.chdir("../")
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs = []
    for doc in docs:
        minimal_doc = Document(
            page_content=doc.page_content,
            metadata={"source": doc.metadata.get("source", "")}
        )
        minimal_docs.append(minimal_doc)
    return minimal_docs

def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk

def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
    )
    return embeddings

# Load and process data
extracted_data = load_pdf_files("data")
minimal_docs = filter_to_minimal_docs(extracted_data)
texts_chunk = text_split(minimal_docs)
embeddings = download_embeddings()

from pinecone import Pinecone
pinecone_api_key = PINECONE_API_KEY

pc = Pinecone(api_key=pinecone_api_key)

from pinecone import ServerlessSpec

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,  # Dimension of the embedding vector
        metric="cosine",  # Similarity metric
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
            # Serverless configuration
    )

index = pc.Index(index_name)

from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embeddings,
    index_name=index_name
)
