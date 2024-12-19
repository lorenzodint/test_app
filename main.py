import streamlit as st

st.set_page_config(layout="wide")

st.write(st.secrets["CUSTOMSTY"], unsafe_allow_html=True)

st.title("TITLO APP")

api = st.secrets["OPENAI_API_KEY"]
st.write(api)
st.write(st.__version__)