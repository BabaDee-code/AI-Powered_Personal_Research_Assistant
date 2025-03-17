import pinecone
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone with your API key from environment variable
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment="us-east-1")

# Create an index
index = pinecone.Index("multilingual-e5-large-index")

def store_embeddings(papers, embeddings):
    for idx, paper in enumerate(papers):
        index.upsert([(paper['title'], embeddings[idx], {"abstract": paper['abstract']})])
