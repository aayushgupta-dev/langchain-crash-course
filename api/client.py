import requests
import streamlit as st


def get_openai_response(text):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": text}}
    )
    return response.json()["output"]["content"]


def get_ollama_response(text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": text}}
    )
    return response.json()["output"]

# streamlit
st.title("Langchain Demo With APIs")
chat_gpt_text = st.text_input("Write an essay on")
ollama_text = st.text_input("Write a poem on")

if chat_gpt_text:
    st.write(get_openai_response(chat_gpt_text))

if ollama_text:
    st.write(get_ollama_response(ollama_text))
