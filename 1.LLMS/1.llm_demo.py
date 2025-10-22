# deprecated LLMs
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# llm model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# prompt
prompt = "What is the capital of India?"

# invoke the model
response = llm.invoke(prompt)
print(response)
