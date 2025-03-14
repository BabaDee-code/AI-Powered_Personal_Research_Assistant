import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# Initialize a Pinecone instance using the new API
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

index_name = "research-papers"

# Check if the index exists, and create it if not
existing_indexes = pc.list_indexes()
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=1536,  # Adjust this to match your embedding dimension
        metric='euclidean',
        spec=ServerlessSpec(cloud='aws', region='us-west-2')
    )

# Retrieve an index instance to perform queries
index = pc.Index(index_name)

def vector_search(query_embedding):
    return index.query(query_embedding, top_k=5)
