import streamlit as st
st.title("Welcome to streamlit")
name=st.text_input("Enter Your Name")
if st.button("Greet Me!"):
    st.write("Hello",name )