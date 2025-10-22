from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
question = input("Please enter your question: ")
response = llm.invoke(question)
print("Response:", response)
print("============================")
print("Response content:", response.content)
