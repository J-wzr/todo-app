import streamlit as st
import functions


todos  = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todo = todo.strip().capitalize() + "\n"
    todos.append(todo)

    functions.add_todos(todos)


st.title("My Todo app")
st.subheader("This app will improve your productivity in your endeavors")



for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.add_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()
    

st.text_input(label="Add todos", placeholder="Enter todo...",
              on_change=add_todo, key="new_todo")
