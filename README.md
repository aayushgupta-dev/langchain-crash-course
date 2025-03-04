# Langchain Crash Course - Chat Bots

This repository is part of the Langchain Crash Course by Krish Naik. It demonstrates how to build and deploy chat bots using two LLM backends:

1. **OpenAI Chat Bot:** Uses the OpenAI API (e.g., GPT-3.5 Turbo) by leveraging your `OPENAI_API_KEY`.
2. **Local Ollama Chat Bot:** Uses a locally installed Ollama model.

The UI for the chat bot is implemented using **Streamlit**, which provides a simple and interactive interface.

## Features

- **Langchain Integration:** Build chains that combine prompts, LLMs, and output parsers.
- **Multiple LLM Backends:** Switch between OpenAI and a locally hosted Ollama model.
- **Interactive UI:** Streamlit-based interface for real-time chat interaction.
- **Environment Management:** Uses `python-dotenv` to load environment variables securely.

## Prerequisites

- **Python 3.8+**
- **Streamlit**
- **Langchain Packages:** Ensure you have installed the correct versions of `langchain_openai`, `langchain_core`, etc.
- **Ollama:** Downloaded and installed on your Windows laptop.
- **API Keys and Environment Variables:**  
  Create a `.env` file in the root directory with the following entries:
  ```dotenv
  OPENAI_API_KEY=your_openai_api_key_here
  LANGSMITH_TRACING=your_tracing_value_here
  LANGCHAIN_API_KEY=your_langchain_api_key_here
