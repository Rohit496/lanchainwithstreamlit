from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import base64
import streamlit as st
from dotenv import load_dotenv
import time

load_dotenv()


def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode()


llm = ChatOpenAI(model="gpt-4o")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64," "{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, width=300)

question = st.text_input("Enter a question")

if question and uploaded_file:
    start_time = time.time()
    image = encode_image(uploaded_file)
    response = chain.invoke({"input": question, "image": image})

    st.write(response.content)
    st.caption(f"⏱️ {time.time() - start_time:.2f}s")
