from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
import streamlit as st


llm = ChatOpenAI(model="gpt-4o")

st.title("Ask Anything")

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
