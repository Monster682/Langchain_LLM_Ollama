# LangChain Demo with Ollama2 API

This project demonstrates the integration of the LangChain framework and the Ollama2 API using Streamlit as the user interface. It serves as a chatbot application where users can input a query, and the system responds with helpful information.

## Features

 **LangChain Integration**: Uses LangChain's prompt templates and output parsers for structured interaction.
- **Ollama2 API**: Leverages the Ollama2 model for generating responses.
- **Streamlit UI**: Provides a simple, interactive web interface for users to input queries.
- **Environment Variable Management**: Utilizes `.env` files to securely store API keys.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
#Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


#Install dependencies:
pip install -r requirements.txt

#Create a .env file in the project root and add the following:
LANGCHAIN_API_KEY=<your_langchain_api_key>
OPENAI_API_KEY=<your_openai_api_key>

#Usage
1-Run the Streamlit application:
2-Open your browser and navigate to
3-Enter a query in the text input box and view the response.

#File Structure
ollama.py: Main application script.
.env: File to store API keys (not included in the repository for security reasons).

#Dependencies
langchain_openai
langchain_core
langchain_community
streamlit
python-dotenv
