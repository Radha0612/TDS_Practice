import streamlit as st

def addition(a,b):
  return(a+b)

st.title("Little Calculator for addition")
a=st.number_input("Enter the first number:")
b=st.number_input("Enter the second number:")

add = addition(a+b)

st.write("The sum of two numbers is :",add)
