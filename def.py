import streamlit as st
import streamlit.components.v1 as components

url = "https://lodi-def.streamlit.app/~/+/"

st.set_page_config(layout="wide")



st.title("Lodi APP")

st.write(st.secrets["OPENAI_API_KEY"])

st.write(f"""<a href="{url}" terget="_self">link</a>""",unsafe_allow_html=True)



st.write("""<p id="par"></p>""", unsafe_allow_html=True)
js="""
         <script>
         function fu() {
         var corrente = window.location.href;
         console.log(corrente);
         document.getElementById("par").innerHTML = corrente;
         }
         fu()
         </script>
         
         """
components.html(js, height=0)

