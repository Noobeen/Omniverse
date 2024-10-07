import pandas as pd 
from pandasai import Agent
from pandasai.llm.local_llm import LocalLLM
import os
import streamlit as st
from Locallm import llm
 
df=pd.read_csv('data.csv')
agent = Agent(
    df,
    description="You are a data analysis agent. Your main goal is to help non-technical users to analyze data",
config={"llm":llm},)
st.title("Hey ask question, create graphs I have a lot data !!!")
question = st.chat_input("Say something")
if question:
    a=agent.chat(question)
    if a=="C:/Users/College_stuffs/spaceapp/Omniverse/exports/charts/temp_chart.png" :
        st.image(a)
    else:
        st.write(a)
else:
    exit    