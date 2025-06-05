
from dotenv import load_dotenv

import streamlit as st
import os
import pathlib

import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "AIzaSyA1m9GD6MDsDz0GeLSKDiSczsqFgzX0_Kw"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question)
    return response
st.set_page_config(page_title="Chatbot_demo")
st.header("Gemini LLM Application")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask The Question")

if submit and input:
    response = get_gemini_response(input)
    st.session_state["chat_history"].append("YOU",input)
    st.subheader("the response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append("BOT",chunk.text)

st.subheader("The Chat History is")
for role,text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")

