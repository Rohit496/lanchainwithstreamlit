from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Agile Coach.Answer any questions "
            "related to the agile process",
        ),
        ("human", "{input}"),
    ]
)

st.title("Agile Guide")

input = st.text_input("Enter the question:")

chain = prompt_template | llm

if input:
    response = chain.invoke({"input": input})
    st.write(response.content)
