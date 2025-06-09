import streamlit as st
import modules.functions

todos = modules.functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    modules.functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input box after adding


st.title("My Todo App")
st.subheader("A simple todo app using Streamlit")
st.write("A simple todo app that allows you to add, edit, and complete todos.")

for todo in todos:
    st.checkbox(todo)

st.text_input("Add a new todo:", placeholder="Enter a new todo here...",
              on_change=add_todo, key="new_todo")

st.session_state