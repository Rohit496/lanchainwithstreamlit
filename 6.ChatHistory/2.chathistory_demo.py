from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
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

chain = prompt_template | llm

history_for_chain = ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)

print("Agile Guide")
print("Type 'exit' or 'quit' to end the conversation\n")

while True:
    question = input("Enter the question: ")
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    if question:
        response = chain_with_history.invoke(
            {"input": question}, {"configurable": {"session_id": "abc123"}}
        )
        print(response.content)
