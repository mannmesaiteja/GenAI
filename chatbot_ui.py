import streamlit as st
import simple_chatbot

st.title("A simple Chatbot for Q&A")

user_input = st.chat_input()

if user_input:
    st.write(user_input)


with st.sidebar:
    st.header("New Chat")
    st.header("Chat History")
    with st.container(border=True):
        st.write("this is inside the container")
        st.write("this is inside the container")
        st.write("this is inside the container")
        st.write("this is inside the container")