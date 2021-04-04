import streamlit as st

st.title("Hello streamlit")
st.subheader(" Streamlit app on streamlit")
x = st.slider('Select a value')
st.write(x, 'second order equation is', x * x + 1)
