# here we are calling llama 3.2:3b
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)
