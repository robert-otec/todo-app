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
st.write("A simple todo app that allows you to add and complete todos.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modules.functions.write_todos(todos)
        del st.session_state[todo]  # Remove the checkbox state
        st.rerun()

st.text_input("Add a new todo:", placeholder="Enter a new todo here...",
              on_change=add_todo, key="new_todo")