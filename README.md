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

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Powered_Personal_Research_Assistant.git
cd AI-Powered_Personal_Research_Assistant
```

### Install Dependencies
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage
To run the Streamlit app, execute:
```bash
streamlit run app.py
```

## Project Structure
- `app.py`: Main application file for the Streamlit app.
- `scraper/`: Contains web scraping spiders for different data sources.
- `summarization/`: Contains the recursive summarization logic.
- `retrieval/`: Contains the BM25 and vector search logic.
- `embeddings/`: Contains scripts for generating and storing embeddings.
- `chunking/`: Contains text chunking logic.
- `.env`: Environment variables file (not included in the repository for security reasons).
- `requirements.txt`: List of dependencies.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License.
