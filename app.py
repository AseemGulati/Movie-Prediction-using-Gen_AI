import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # activate the api
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API'))

# Movie Recomender system
st.title('Movie Recommender System !!')
user_input=st.text_input('Enter the Movie Name')
submit=st.button('Click Here')

model=genai.GenerativeModel('gemini-1.5-flash-002')

if submit:
    response=model.generate_content(f'Generate Movie Reconmendation for {user_input}')
    st.write(f'Recomendations:\n {response.text}')
else:
    st.write(' ')
