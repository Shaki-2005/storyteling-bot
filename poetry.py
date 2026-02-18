
import streamlit as st
import pandas as pd 
import time
from google import genai

def cook_food(prompt):
    if prompt:
        msg = st.toast("Gathering words")
        time.sleep(2)
        msg = st.toast("creating")
        time.sleep(2)
        msg = st.toast("Ready!", icon="🥞")
        time.sleep(2)
        st.write(f"So you want to generate a poem {prompt}")
        time.sleep(1)
        st.write("Let's see how much you like it.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a summarized poetry {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyBuJGXZSHirZ2chL-SuCXYYg_v8c9znIhE"   # YOUR API
    # initialize the client
    client = genai.Client(api_key=API_KEY)
    # title 
    st.title("poetry generator")
    prompt = st.chat_input("What's your mood?")
    cook_food(prompt)