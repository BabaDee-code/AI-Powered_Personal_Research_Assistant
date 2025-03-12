import pinecone
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone with your API key from environment variable
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment="us-west1-gcp")

# Create an index
index = pinecone.Index("research-papers")

def vector_search(query_embedding):
    return index.query(query_embedding, top_k=5)
