import streamlit as st
import pandas as pd
import numpy as np

from src.pydeck_builders import BuildDeckRenderer


class BuildStreamlitMainPage:
    def __call__(self):
        st.set_page_config(layout="wide")

        minimum_sequence_identity = st.slider(
            label="Minimum sequence identity",
            key="minimum_sequence_identity",
            min_value=0.9995,
            max_value=0.9999,
            value=0.9995,
            step=0.0001,
            format=f"%.4f",
            help="To be the same cluster (color), how similar do two androgen receptors need to be?",
        )
        # st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
        st.pydeck_chart(BuildDeckRenderer()(minimum_sequence_identity))


BuildStreamlitMainPage()()
