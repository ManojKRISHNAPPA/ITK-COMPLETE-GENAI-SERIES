import streamlit as st
import os 

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="ITK Chat app",
    page_icon= "🥃"
)

st.title("Ollama Chatbot")

temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.slider("Max Tokens", 100, 1000, 100)

input_text = st.text_input("Ask your question...")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are helpfull assitant."),
        ("user","Question: {question} ")
    ]
)

llm = Ollama(
    temperature=temperature,
    model="llama3.1:latest"
)


output_parser = StrOutputParser()
chain  = prompt| llm | output_parser


if input_text:
    response = chain.invoke({"question":input_text})
    st.write(response)

