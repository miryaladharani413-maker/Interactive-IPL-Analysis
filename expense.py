import streamlit as st
import requests
st.title("Joke ADD")
if st.button("Get Joke"):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    st.write(f"{data['setup']}")
    st.write(f"{data['punchline']}")