from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


llm = OpenAIEmbeddings()

text = input("Enter the text")
response = llm.embed_query(text)
print(response)
