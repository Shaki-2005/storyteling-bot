import streamlit as st
import time
from google import genai

def tell_story(prompt):
    if prompt:
        msg = st.toast("Walking into the hills...")
        time.sleep(2)

        msg = st.toast("Listening to the wind...")
        time.sleep(2)

        msg = st.toast("A story is unfolding...", icon="🌿")
        time.sleep(2)

        st.write(f"You asked for a story about: **{prompt}**")
        time.sleep(1)
        st.write("Let us travel to a quiet hill station...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Write a short nostalgic story inspired by Ruskin Bond.
            Keep the language simple, warm, and descriptive.
            Include nature, emotions, small-town life, and gentle life lessons.
            Theme: {prompt}
            """
        )

        st.write(response.text)


if __name__ == "__main__":
    API_KEY = "AIzaSyBuJGXZSHirZ2chL-SuCXYYg_v8c9znIhE"  
    client = genai.Client(api_key=API_KEY)

    st.title("🌿 Hillside Storyteller")
    st.subheader("Stories inspired by Ruskin Bond")

    prompt = st.chat_input("What kind of story would you like to hear? (rain, childhood, mountains...)")

    tell_story(prompt)