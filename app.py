from langchain.llms import OpenAI 
from dotenv import load_dotenv
import os ,sys 
import streamlit as st

load_dotenv()
KEY = os.getenv("OPENAI_API_KEY") #you can use os.environ.get("OPENAI_API_KEY")
model_name = 'gpt-3.5-turbo-0125'
temperature=0.5


def get_openai_response(question):
    llm = OpenAI(model_name =  model_name, temperature=temperature) 
    response = llm(question)
    return response


#Start streamlit 
st.set_page_config(page_title='Q&A Demo')

st.header('Langchain Q&A Application')
input_text = st.text_input("Question:" ,key='input')
response = get_openai_response(question=input_text)


st.button('Ask The Question')

if st.button:
    st.subheader('The Response is ')
    st.write(response)