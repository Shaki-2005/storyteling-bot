import streamlit as st 
import pandas as pd
import ollama 
import time

def generate_recipe(input):
    """Cleaner task for single-shot tasks."""
    response = ollama.generate(model="gemma3:4b", prompt="Complete this code in python :{input}")
    return response.response

def load_app():
    with st.form("input"):
        input = st.text_input("Enter code here")
        submit = st.form_submit_button("Complete")
    
    # if submit:           # if the submit button is clicked
    #     msg = st.toast("Gathering ingredients...")
    #     time.sleep(2)
    #     msg = st.toast("Cooking...")
    #     time.sleep(2)
    #     msg = st.toast("Ready!", icon="🥞")
    #     time.sleep(2)
        st.write(generate_recipe(input))

load_app()