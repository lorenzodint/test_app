import streamlit as st
import streamlit.components.v1 as components

url = "https://lodi-def.streamlit.app/~/+/"

st.set_page_config(layout="wide")



st.title("Lodi APP")

st.write(st.secrets["OPENAI_API_KEY"])

st.write(f"""<a href="{url}" terget="_self">link</a>""",unsafe_allow_html=True)



st.write("""<p id="par"></p>""", unsafe_allow_html=True)
js="""
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
         <script>
         function fu() {
         var corrente = window.location.href;
         console.log(corrente);
         window.location.href = "https://it.wikipedia.org/wiki/Associazione_sportiva_dilettantistica";
         }
        function myFunction() {
            //location.assign("https://www.google.co.in");
            window.location.replace("https://www.google.co.in");
        }
        function countElementsWithSameId(id) {
            // Seleziona tutti gli elementi con l'ID specificato
            var elements = document.querySelectorAll(`[class="${id}"]`);
            // Conta il numero di elementi trovati
            var count = elements.length;
            console.log(`Numero di elementi con l'ID "${id}":`, count);
            return count;
        }

        // Esegui la funzione per contare gli elementi con l'ID "myElement"
        countElementsWithSameId('_streamlitAppContainer_nim44_1');
        </script>
         
         """
         
         
js = """
 <script>
        // Ascolta i messaggi dal documento principale
        window.addEventListener('message', function(event) {
            if (event.origin !== 'https://lorenzodintino.altervista.org/STREAMLIT.php') {
                return;
            }
            if (event.data === 'addDiv') {
                var newDiv = document.createElement('div');
                newDiv.textContent = 'Questo è un div in IFRAME';
                document.body.appendChild(newDiv);
            }
        });
    </script>
"""
components.html(js, height=0)

