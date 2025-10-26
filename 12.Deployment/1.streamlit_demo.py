from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from openai import api_key
import streamlit as st

load_dotenv()

st.title("Ask Anything")

# Sidebar for API key
with st.sidebar:
    st.title("Provide Your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.error("Enter your OpenAI API Key to Continue")
    st.stop()

question = st.text_input("Enter the question:")
ask_button = st.button("Ask")

if ask_button and question:
    if OPENAI_API_KEY:
        llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
        with st.spinner("Thinking..."):
            response = llm.invoke(question)
        st.write(response.content)
    else:
        st.warning("Please enter your API key in the sidebar!")
