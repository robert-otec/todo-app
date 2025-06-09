import streamlit as st
import modules.functions

todos = modules.functions.get_todos()

st.title("My Todo App")
st.subheader("A simple todo app using Streamlit")
st.write("This is a simple todo app that allows you to add, edit, and complete todos.")

for todo in todos:
    st.checkbox(todo)

st.text_input("Add a new todo:", placeholder="Enter a new todo here...")