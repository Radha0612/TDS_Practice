import streamlit as st

def large(a,b,c):
  if (a >= b) and (a >=c):
     return(a)
  if (b>=a) and (b>=c) :
    return(b)
  if (c>=a) and (c>=b):
    return(c)

st.title("LARGEST OF THE 3 NUMBERS")
a=st.number_input("Enter the first Number:")
b=st.number_input("Enter the second Number:")
c=st.number_input("Enter the third Number:")

out=large(a,b,c)

if st.button("Submit"):
   st.write("The largest number is ",out)
