from helpers import *
import streamlit as st

st.title("cal of two num")

n1 =int(st.number_input("n1:"))
#n1 = int(input("n1:"))
n2 = int(st.number_input("n2:"))
#n2 = int(input("n2:"))

operator = st.selectbox("select operation", ['Add','Subraction','Multiply',"Division",'Power','Floor'])

# a=st.button("click")
# st.write(a)
if st.button("Show"):

    if operator == 'Add':
        st.write(add(n1, n2))
    elif operator == 'Subraction':
        st.write(sub(n1, n2))
    elif operator == 'Multiply':
        st.write(mull(n1, n2))
    elif operator == 'Power':
        st.write(power(n1, n2))
    elif operator == 'Division':
        st.write(division(n1, n2))
    elif operator == 'Floor':
        st.write(floor(n1,n2))
    else:
        st.write("invalid input")