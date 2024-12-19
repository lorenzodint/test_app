import streamlit as st
import os

st.set_page_config(layout="wide")

# IMPORT CSS
def local_css(fileName):
    with open(fileName) as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(st.secrets["CUSTOMSTY"])

st.title("TITLO APP LODI")

api = st.secrets["OPENAI_API_KEY"]
st.write(api)
st.write(st.__version__)