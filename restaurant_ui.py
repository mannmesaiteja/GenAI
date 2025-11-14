import streamlit as st

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("pick a cuisine", ("Indian", "American", "Mexican", "Italian")) # store the selected item in a variable


def generate_restaurant_and_items(cu):
    return (
        {
            "restaurant_name": "Venkateswara_Restaurant",
            "menu_items": "Biriyani, Fried Chicken, Mutton Curry, Full meals"
        }
    )

if cuisine:
    res = generate_restaurant_and_items(cuisine)
    st.header(res['restaurant_name'])
    st.write("**Menu Items**")
    items = res['menu_items'].split(",")
    for i in items:
        st.write("-", i)