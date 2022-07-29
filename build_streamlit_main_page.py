import streamlit as st
import pandas as pd
import numpy as np

from src.pydeck.arc_layer import build_deck_renderer


class BuildStreamlitMainPage:
    def __call__(self):
        st.set_page_config(layout="wide")

        minimum_sequence_identity = st.slider(
            label="Minimum sequence identity",
            key="minimum_sequence_identity",
            min_value=0.950,
            max_value=0.995,
            value=0.950,
            step=0.005,
            format=f"%.3f",
            help="To be the same cluster (color), how similar do two androgen receptors need to be?",
        )
        # st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
        st.pydeck_chart(build_deck_renderer(minimum_sequence_identity))


BuildStreamlitMainPage()()
