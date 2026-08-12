from jinja2 import environment
import streamlit as st

st.set_page_config(
    page_title="ITK app",
    page_icon= "🥃"
)

st.title("ITK Employee Managment")

name = st.text_input("Employee Name")
age = st.number_input(
    "Age",
    min_value = 18,
    max_value = 100
)

role = st.selectbox(
    "Role",
    ["devops","python dev","Ai Engineer"]
)

if st.button("submit"):
    st.success("Employee Created..!")

    st.write("Name: ", name)
    st.write("Age: ", age)
    st.write("Role: ", role)

debug  = st.checkbox("Enable debugging")


col1,col2 = st.columns(2)


with col1:
    st.metric("Cpu","70%")

with col2:
    st.metric("Memory","65%")

with st.sidebar:
    st.header("configurations")

    environment = st.selectbox(
        "Environment",
        ["DEV","Stage","Prod"]
    )

    debug  = st.checkbox("Enable debugging")

with st.container():
    st.header("Employee Information")

    st.write("name: Manoj")
    st.write("Role: AI engineer")


import pandas as pd

data = {
    "Name": ["Manoj", "Rahul", "Priya"],
    "Role": ["DevOps", "Python", "AI"]
}

df = pd.DataFrame(data)

st.dataframe(df)

uploaded_file = st.file_uploader(
    "Upload a PDF"
)