import pandas as pd 
from pandasai import Agent
from pandasai.llm.local_llm import LocalLLM
import os
import streamlit as st
#from langchain_ollama import ChatOllama
from Locallm import llm
 
df=pd.read_csv('txt.csv')

agent = Agent(
    df,
    description="You are a data analysis agent. Your main goal is to help non-technical users to analyze data",
    config={"llm":llm}
)
st.title("Visualization tool")
question = st.chat_input("Say something")
if question:
    a=agent.chat(question)
    if a==
    st.write(a)
    st.image(a)
else:
    exit    