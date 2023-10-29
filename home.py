import streamlit as st
import functions

st.title("My Todo app")
st.subheader("This app will improve your productivity in your endeavors")


todos  = functions.get_todos()
for item in todos:
    st.checkbox(item)