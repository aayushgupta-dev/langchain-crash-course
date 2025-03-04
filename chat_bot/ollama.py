from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# load env variables
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my helpful assistant. Please respond to my queries"),
    ("user", "Question: {question}")
])

# streamlit ui
st.title("Langchain with Llama 3")
input_text = st.text_input("Search the topic u want")

# define chain - loading model from local machine : download ollama; run : ollama run llama3.2:1b; 
LLM = Ollama(model="llama3.2:1b")
output_parser = StrOutputParser()
chain = prompt | LLM | output_parser

# chat via bot
if input_text: 
    st.write(chain.invoke({ "question": input_text }))