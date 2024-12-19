import streamlit as st

st.set_page_config(layout="wide")


st.title("TITLO APP")

api = st.secrets["OPENAI_API_KEY"]
st.write(api)