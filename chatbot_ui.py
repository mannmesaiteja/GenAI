import streamlit as st
import requests
from db_configuration import db_connection
from pprint import pprint



st.title("A simple Chatbot for Q&A")


# user_input = st.chat_input()
#
# if user_input:
#     st.write(user_input)

user_input = st.chat_input()

if user_input:
    try:
        st.write("You:", user_input)
        response = requests.post("http://127.0.0.1:8000/generate", json={"question": user_input}).json()
        # pprint(response)
        if "error" in response:
            st.error(response['error'])
        else:
            st.write(response['message'])
            try:
                con = db_connection()
                cursor = con.cursor()
                print(type(response['response_time']))
                cursor.execute(
                    "insert into chatbot (querys, response, api_hit_time, responsetime) values (%s, %s, %s, %s)",
                    (user_input, response["message"], response['start_date_time'], response['response_time'])
                )
                con.commit()
            except Exception as e:
                print("exception at insertion:", str(e))
            finally:
                cursor.close()
                con.close()
    except Exception as e:
        print("Exception at response:", str(e))







with st.sidebar:
    st.header("New Chat")
    st.header("Chat History")
    with st.container(border=True):
        st.write("this is inside the container")
        st.write("this is inside the container")
        st.write("this is inside the container")
        st.write("this is inside the container")


