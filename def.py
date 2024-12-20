
# import src.functions
import sys
import importlib.util
import requests
import streamlit.components.v1 as components
import streamlit as st
print("sono main")
# import src.functions as func

st.set_page_config(layout="wide")

files = [
    st.secrets['FUNZIONI'],
    st.secrets['FU'],
]

modules = {}

for file in files:
    response = requests.get(file)
    file_name = file.split("/")[-1]
    namespace = {}
    
    exec(response.text, namespace)
    
    module_name = file_name.replace('.py', '')
    modules[module_name] = namespace
    
    
    
    
# exec(response.text, namespace)

url = "https://lodi-def.streamlit.app/~/+/"

st.title("Lodi APP")

st.write(st.secrets["OPENAI_API_KEY"])

js = """
    
    """
components.html(js, height=0)

# namespace['scrivi']("ciao")

modules["functions"]["scrivi"]("ciao")



if st.button("bottone"):
    modules["fu"]["saluta"]()
