import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to ProjetData")


    contrat = st.selectbox('Type de contrat', ["","CDD","CDI"])
    if  contrat == "":
        st.warning('Veuillez selelctionner un type de contrat.')

    code_postal = st.number_input('Code Postal', step=1, value=None)
    if len(str(code_postal)) != 5 and code_postal != None:
        st.warning('Veuillez entrer un code postal valide.')


if __name__ == "__main__":
    run()
