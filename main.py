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
        st.write(content)
    else:
        st.write(f"errore: {response.status_code}")


style(st.secrets["CUSTOMSTY"])

st.write("""<script>var element = document.getElementById('root');
            element.classList.add('AGGIUNTO');</script>""")


st.write("""
         <div class="mioFooter">FOOTER</div>
         """, unsafe_allow_html=True)



st.title("TITLO APP LODI")


api = st.secrets["OPENAI_API_KEY"]
st.write(api)
st.write(st.__version__)


if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'
    
    
    
if st.session_state.pagina == "home":
    if st.button("vai a contatti"):
        st.header(":blue HOME")
        st.session_state.pagina = "contatti"
if st.session_state.pagina == "contatti":
    if st.button("torna a home"):
        st.header(":red CONTATTI")
        st.session_state.pagina = "home"