
'''
name = input("Enter you name: ")
print(f" Hello Welcome {name}")

start --> take input--> Process --> print output --> end
'''


import streamlit as st

st.title("ITK first application...")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello welcome to streamlit genertaed {name}")