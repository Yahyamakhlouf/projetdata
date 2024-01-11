# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to ProjetData")

    contrat = st.multiselect('Type de contrat', ["CDD","CDI","Intérim","Stage","Apprentissage","Contrat pro","Indépendant"], default=[])

    code_postal = st.number_input('Code Postal', step=1, value=None)

    secteur = st.text_input('Secteur')
    
    if st.button('Valider'):
            # Vérifier si le type de contrat est vide
            if  contrat == "":
                st.warning('Veuillez selelctionner un type de contrat.')
            # Vérifier si le code postal est vide
            if  code_postal == None:
                st.warning('Veuillez entrer un code postal.')
            # Vérifier si le code postal est valide
            if len(str(code_postal)) != 5 and code_postal != None:
                st.warning('Veuillez entrer un code postal valide.')
            


if __name__ == "__main__":
    run()

