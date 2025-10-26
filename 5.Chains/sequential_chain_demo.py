from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model="gpt-4o")
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are an experienced speech writer.
    You need to craft an impactful title for a speech 
    on the following topic: {topic}
    Answer exactly with one title.	
    """,
)

speech_prompt = PromptTemplate(
    input_variables=["title", "emotion"],
    template="""You need to write a powerful {emotion} speech of 350 words
     for the following title: {title} 
     Format the output with 3 keys: 'title', 'emotion' and 'speech' and fill them with the respective values
    """,
)

first_chain = (
    title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
)
second_chain = speech_prompt | llm
final_chain = (
    first_chain
    | (lambda title: {"title": title, "emotion": emotion})
    | second_chain
    | JsonOutputParser()
)

st.title("Speech Generator")

topic = st.text_input("Enter the topic:")
emotion = st.text_input("Enter the emotion:")

if topic and emotion:
    with st.spinner("Generating speech title and content..."):
        response = final_chain.invoke({"topic": topic, "emotion": emotion})
        st.write(response)
        # divider
        st.markdown("---")
        st.write(response["title"])
        st.markdown("---")
        st.write(response["emotion"])
        st.markdown("---")
        st.write(response["speech"])
