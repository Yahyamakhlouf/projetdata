import streamlit as st
import pandas as pd
import pydeck as pdk

from urllib.error import URLError
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to ProjetData")


    contrat = st.selectbox('Type de contrat', ["","CDD","CDI","Stage","Alternance"])
    if  contrat == "":
        st.warning('Veuillez selelctionner un type de contrat.')

    code_postal = st.number_input('Code Postal', step=1, value=None)
    if len(str(code_postal)) != 5 and code_postal != None:
        st.warning('Veuillez entrer un code postal valide.')

    


#La carte graphique
def mapping_demo():
    @st.cache_data
    def from_data_file(filename):
        url = (
            "https://github.com/PDECM/projetdata/tree/Mayssa" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("BDD.json"),
                get_position=["longitude_lieuTravail", "latitude_lieuTravail"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("BDD.json"),
                get_position=["longitude_lieuTravail", "latitude_lieuTravail"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("BDD.json"),
                get_position=["longitude_lieuTravail", "latitude_lieuTravail"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=10,
                get_alignment_baseline="'bottom'",
            )
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


if __name__ == "__main__":
    try:
        run()
        mapping_demo()
    except Exception as e:
        st.error(f"An error occurred: {e}")
