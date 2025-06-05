from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in data science and a helpful assistant. Your task is to provide clear, concise, and easy-to-understand responses to user queries. Always be polite, encouraging, and patient, especially with beginners. Ensure that your explanations are step-by-step and avoid using jargon unless it is explained in simple terms. Provide examples wherever possible to illustrate concepts.",
        ),
        ("user", "Question:{question}"),
    ]
)

st.title("LLM using OLLAMA")
input_text = st.text_input("Search the topic you want🙌")

llm = Ollama(model="llama2:7b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))