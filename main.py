import streamlit as st
import os
import requests
from streamlit_navigation_bar import st_navbar

st.set_page_config(layout="wide")

# IMPORT CSS
def style(url):
    response = requests.post(url)
    if response.status_code == 200:
        content = response.text
        st.write(f"<style>{content}</style>", unsafe_allow_html=True)
        # st.write(content)
    else:
        st.write(f"errore: {response.status_code}")


style(st.secrets["CUSTOMSTY"])



page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)