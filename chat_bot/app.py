from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# load env variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my helpful assistant. Please respond to my queries"),
    ("user", "Question: {question}")
])

# streamlit ui
st.title("Langchain with Open AI")
input_text = st.text_input("Search the topic u want")

# define chain - loading model from cloud : sign up to openai; get your api keys; 
LLM = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | LLM | output_parser

# chat via bot
if input_text: 
    st.write(chain.invoke({ "question": input_text }))