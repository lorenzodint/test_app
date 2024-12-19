import streamlit as st
import os
import requests

st.set_page_config(layout="wide")

# IMPORT CSS
def style(url):
    response = requests.post(url)
    if response.status_code == 200:
        content = response.text
        st.write(f"<style>{content}</style>", unsafe_allow_html=True)
    else:
        st.write(f"errore: {response.status_code}")


style(st.secrets["CUSTOMSTY"])
# st.write("""<style>.stAppHeader {display: none;}._profileContainer_gzau3_53{display: none;}</style>""", unsafe_allow_html=True)


st.title("TITLO APP LODI")

api = st.secrets["OPENAI_API_KEY"]
st.write(api)
st.write(st.__version__)