import streamlit as st
import os
import requests
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import webbrowser

st.set_page_config(layout="wide")

url = "https://lorenzodintino.altervista.org/STREAMLIT.php"

# components.iframe("https://lodi-test.streamlit.app/~/+/") UTILE PER MOSTRARE PAGINE WEB ALL INTERNO DEL SITO

# Codice HTML con JavaScript per ottenere l'URL corrente e reindirizzare
# html_code = """
# <script>
# function checkAndRedirect() {
#     var currentUrl = window.location.href;
#     console.log("Current URL:", currentUrl);

#     // Condizione per il reindirizzamento
#     if (currentUrl != "https://lodi-test.streamlit.app/~/+/" || currentUrl == "about:srcdoc") {
#         window.location.href = "https://lodi-test.streamlit.app/~/+/";
#     }
# }

# function removeHeader() {
#             var headers = document.getElementsByTagName('header');
#             if (headers.length > 0) {
#                 headers[0].remove();
#             }
#         }


# window.onload = function() {
#             window.location.href = 'https://lodi-test.streamlit.app/~/+/';
#         };
# </script>
# """
# # Inserire il componente HTML nella tua app Streamlit
# components.html(html_code, height=0)


html = """
            <script>
                function removeSandbox() {
            // Seleziona l'iframe utilizzando il titolo
            //var iframe = document.querySelector('iframe[title="streamlitApp"]');
            var iframe = document.querySelector('._container_gzau3_1');
            if (iframe) {
                //iframe.removeAttribute('sandbox');
                iframe.classlist.add("togli");
                console.log('Sandbox rimosso da iframe.');
            } else {
                console.log('Iframe non trovato.');
            }
        }

        // Esegui la funzione quando la pagina è caricata
        window.onload = removeSandbox();
        removeSandbox()
            </script>
            """
components.html(html, height=0)

# st.markdown(
#         f"""
#         <meta http-equiv="refresh" content="0;URL='{url}'" />
#         """,
#         unsafe_allow_html=True
#     )


# Allow iframes to open top-level windows
markup = '''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("iframe", window.parent.document).each(function(){
        const st_iframe = $(this);
        st_iframe.attr('sandbox', 'allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads allow-top-navigation allow-top-navigation-by-user-activation');
    });
    $("base").attr("target", "_top");
    alert('iframe tweaked!!!');
    window.top.location.href = "https://lorenzodintino.altervista.org/STREAMLIT.php";
});
</script>
'''
# components.html(markup)
# components.html(html, height=0)

price = "98765"

st.markdown(f"""
                    st.markdown('Please <a href="https://www.html.it/pag/15220/operatori1/" target="_self">click</a>')
                """, unsafe_allow_html=True)


# Funzione per reindirizzare a un URL esterno
def redirect_to_url(url):
    st.markdown(
        f"""
        <script>
            window.onload = function() {{
                window.top.location.href = '{url}';
            }};
        </script>
        """,
        unsafe_allow_html=True
    )

# URL esterno a cui vuoi reindirizzare
external_url = "https://google.com"

# Chiama la funzione per reindirizzare
redirect_to_url(external_url)




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


st.title("Il mio Sito")
st.link_button("avvia", url)
   
    


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
