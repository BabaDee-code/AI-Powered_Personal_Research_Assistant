import os
import streamlit as st
from scraper.arxiv_spider import ArxivSpider
from embeddings.generate_embeddings import generate_embeddings
from retrieval.bm25_search import bm25_search
from retrieval.vector_search import vector_search
from summarization.recursive_summary import recursive_summarization
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set Pinecone API key from environment variable
from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pinecone = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

def main():
    st.title("AI-Powered Research Assistant")

    query = st.text_input("Enter your research query")

    if query:
        # Step 1: Retrieve papers (use scraping, BM25, and Vector Search)
        papers = ArxivSpider().parse(query)  # You may want to modify this method to take query as input
        embeddings = generate_embeddings([paper['abstract'] for paper in papers])

        # Step 2: Hybrid search (BM25 + Vector Search)
        bm25_results = bm25_search(query, [paper['abstract'] for paper in papers])
        vector_results = vector_search(embeddings)
        
        # Combine results
        combined_results = bm25_results + vector_results

        # Step 3: Summarize
        paper_sections = [paper['abstract'] for paper in combined_results]
        summary = recursive_summarization(paper_sections)

        # Display Results
        st.write("Summarized Research:")
        st.write(summary)

if __name__ == "__main__":
    main()