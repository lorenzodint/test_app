import streamlit as st
import os
import requests
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# components.iframe("https://lodi-test.streamlit.app/~/+/") UTILE PER MOSTRARE PAGINE WEB ALL INTERNO DEL SITO

# Codice HTML con JavaScript per ottenere l'URL corrente e reindirizzare
html_code = """
<script>
function checkAndRedirect() {
    var currentUrl = window.location.href;
    console.log("Current URL:", currentUrl);

    // Condizione per il reindirizzamento
    if (currentUrl != "https://lodi-test.streamlit.app/~/+/")) {
        window.location.href = "https://lodi-test.streamlit.app/~/+/";
    }
}
window.onload = checkAndRedirect;
</script>
"""
# Inserire il componente HTML nella tua app Streamlit
components.html(html_code, height=0)


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





# selected = option_menu(
#     menu_title=None,
#     options=["home", "progetti", "contatti"],
#     icons=["house", "book", "envelope"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
# )

# if selected == "home":
#     st.title("HOME")
# if selected == "progetti":
#     st.title("PROGETTI")
# if selected == "contatti":
#     st.title("CONTATTI")