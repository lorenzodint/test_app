import streamlit as st
import streamlit.components.v1 as components
# import src.functions as func
import requests
import importlib.util
import sys

st.set_page_config(layout="wide")



response = requests.get(st.secrets["IMPORT_FILE"])

namespace = {}

exec(response.text, namespace)

url = "https://lodi-def.streamlit.app/~/+/"




st.title("Lodi APP")

st.write(st.secrets["OPENAI_API_KEY"])


         
js = """
 
"""
components.html(js, height=0)

namespace['scrivi']("ciao")
# scrivi("ciao")
