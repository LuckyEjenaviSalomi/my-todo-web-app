import streamlit as st
import functions

functions.create_file()
todos = functions.read_todos()


def add_todo():
    todo_ = st.session_state['new_todo'].strip() + '\n'
    if todo_ not in todos:
        todos.append(todo_)
        functions.write_todos(todos)


st.title("My Todo App")
st.subheader('This is my to-do app')
st.write("This app is to improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='#', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
