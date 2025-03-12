import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_embeddings(texts):
    response = openai.Embedding.create(
        model="text-embedding-ada-002", 
        input=texts
    )
    embeddings = [embedding['embedding'] for embedding in response['data']]
    return embeddings
