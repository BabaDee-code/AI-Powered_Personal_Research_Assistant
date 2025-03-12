# AI-Powered Personal Research Assistant (RAG Project)

## Overview
This project implements an AI-powered research assistant that retrieves and summarizes academic research papers based on user queries. It integrates multiple data sources like **arXiv**, **PubMed**, and **SSRN**, using a hybrid retrieval system combining **BM25** and **vector similarity search** (via **Pinecone**). The system generates concise summaries of relevant research papers using **OpenAI’s GPT models**, leveraging a recursive summarization approach.

The system provides an interactive **Streamlit** app where users can input research topics and receive real-time summaries of related academic papers.

## Features
- **Hybrid Retrieval System**: Combines **BM25** keyword search with **Pinecone** vector search to retrieve relevant papers.
- **Summarization**: Uses **OpenAI's GPT-4** for recursive summarization of research papers.
- **Interactive UI**: A **Streamlit** app for user input and real-time responses.
- **API Key Management**: Secure management of API keys using **environment variables** and **python-dotenv**.

## Requirements
- Python 3.7+
- Install dependencies via `pip install -r requirements.txt`.

### Install Dependencies
To install the required dependencies, run:
```bash
pip install -r requirements.txt
