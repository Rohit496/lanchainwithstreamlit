from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

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
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt_template | llm | StrOutputParser()

history_for_chain = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)


def chat_with_llm(input_text):
    for output in chain_with_history.stream(
        {"input": input_text}, {"configurable": {"session_id": "abc123"}}
    ):
        yield output


st.title("Agile Guide")

input = st.text_input("Enter the question:")

if input:
    response = st.write_stream(chat_with_llm(input))

st.write("HISTORY")
st.write(history_for_chain)
