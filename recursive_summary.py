import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def recursive_summarization(paper_sections):
    summary = ""
    for section in paper_sections:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Summarize this section: {section}",
            max_tokens=100
        )
        summary += response['choices'][0]['text']
    return summary
