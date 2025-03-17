# app/app.py
import os
import streamlit as st
from scraper.arxiv_scraper import fetch_recent_papers
from embeddings.generate_embeddings import generate_embeddings
from retrieval.bm25_search import bm25_search
from retrieval.vector_search import vector_search
from summarization.recursive_summary import recursive_summarization
from dotenv import load_dotenv
from database import init_db

# Load environment variables and initialize the database.
load_dotenv()
init_db()

# Set OpenAI API key from environment variable
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set Pinecone API key and connect to the existing index
from pinecone import Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index_name = "multilingual-e5-large-index" 
index = pc.Index(index_name)

def main():
    st.title("AI-Powered Research Assistant")
    query = st.text_input("Enter your research query")
    
    if query:
        # Fetch recent papers and store them in the database.
        papers = fetch_recent_papers()
        if not papers:
            st.write("No papers found. Please try again later.")
            return

        # Generate embeddings for each paper's abstract.
        embeddings = generate_embeddings([paper['abstract'] for paper in papers])
        bm25_results = bm25_search(query, [paper['abstract'] for paper in papers])
        vector_results = vector_search(embeddings)
        
        # Combine results (simple concatenation; you may need to refine this logic).
        combined_results = bm25_results + vector_results
        paper_sections = [paper['abstract'] for paper in combined_results]
        summary = recursive_summarization(paper_sections)
        
        st.write("Summarized Research:")
        st.write(summary)

if __name__ == "__main__":
    main()
