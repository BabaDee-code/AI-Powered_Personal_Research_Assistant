import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

# Initialize a Pinecone instance using the new API
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# Use the exact name of your existing index
index_name = "multilingual-e5-large-index"

# Simply connect to the existing index
index = pc.Index(index_name)

def vector_search(query_embedding):
    return index.query(query_embedding, top_k=5)
