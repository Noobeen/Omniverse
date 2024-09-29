import numpy as np
import os
import pandas as pd
from pandasai import Agent
from pandasai.llm.local_llm import LocalLLM
import streamlit as st
from key import pd_key # to get Api_key from user

#Assinging API Key
os.environ["PANDASAI_API_KEY"]=pd_key

st.title("Omniverse")


#Taking sample data and create pandas data frame
data = pd.read_csv('txt.csv')

#Creating agent
agent = Agent(data)

#Prompt
hist=""
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

    a=agent.chat(prompt)
    hist=hist+"  "+prompt

    st.header(a)
else:
    exit

