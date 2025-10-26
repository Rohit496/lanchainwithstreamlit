from langchain_openai import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv

load_dotenv()

llm = OpenAIEmbeddings()

text1 = input("Enter the text1")
text2 = input("Enter the text2")

response1 = llm.embed_query(text1)
response2 = llm.embed_query(text2)

similarity_score = np.dot(response1, response2)

print(similarity_score * 100, "%")
