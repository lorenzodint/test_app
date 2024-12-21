import src.functions
###################################################################################################
import sys
import importlib.util
import requests
import streamlit.components.v1 as components
import streamlit as st



st.set_page_config(layout="wide")

files = [
    st.secrets['FUNZIONI'],
    st.secrets['FU'],
    st.secrets['HOME'],
]

modules = {}

for file in files:
    response = requests.get(file)
    file_name = file.split("/")[-1]
    namespace = {}
    
    exec(response.text, namespace)
    
    module_name = file_name.replace('.py', '')
    modules[module_name] = namespace
    
    
    
    



st.title("App")

# st.write(st.secrets["OPENAI_API_KEY"])

js = """
    
    """
# components.html(js, height=0)



# modules["functions"]["scrivi"]("ciao")



# if st.button("bottone"):
#     modules["fu"]["saluta"]()
    
###################################################################
if "page" not in st.session_state:
    st.session_state.page = "login"
if "chiLoggato" not in st.session_state:
    st.session_state.chiLoggato = "0"
    
    

modules['home']['mostra']()


    
# st.write(st.session_state)
