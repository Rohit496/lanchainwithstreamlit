from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.globals import set_debug

set_debug(True)


load_dotenv()
llm = ChatOpenAI(model="gpt-4o")
st.title("Ask Anything")

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
