import pandas as pd 
from pandasai import Agent
from pandasai.llm.local_llm import LocalLLM
import os
import streamlit as st
from langchain_ollama import ChatOllama
 

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

df=pd.read_csv('txt.csv')

agent = Agent(df,config={"llm":llm})
st.title("Visualization tool")
question = st.chat_input("Say something")
if question:
    st.header(agent.chat(question))
else:
    exit    