from dotenv import load_dotenv
import os
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from pinecone import Pinecone
pinecone_api_key = PINECONE_API_KEY

pc = Pinecone(api_key=pinecone_api_key)
pc
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
#Load Existing Index

from langchain_pinecone import PineconeVectorStore
#Embed each chunk and upsert the embeddings to the Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
