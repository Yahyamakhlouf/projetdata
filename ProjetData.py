import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def from_data_file(filename):
    url = (
        "https://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)

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

    st.pydeck_chart(
            Deck(
                map_style=None,
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        )
            )
        )

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        st.error(f"An error occurred: {e}")
