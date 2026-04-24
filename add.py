import streamlit as st

st.title("Simple Python App")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", step=1)

if st.button("Submit"):
    st.write("Hello", name)
    st.write("You are", age, "years old")