from dotenv import load_dotenv

load_dotenv()
from langchain_ollama import ChatOllama


base_url = "http://localhost:11434"
model = "llama3.2:latest"

llm = ChatOllama(model=model, base_url=base_url)
question = input("Please enter your question: ")
response = llm.invoke(question)
print("Response:", response)
print("============================")
print("Response content:", response.content)
