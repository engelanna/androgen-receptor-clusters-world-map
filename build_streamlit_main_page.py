import streamlit as st
import pandas as pd
import numpy as np

from src.pydeck_builders import BuildDeckRenderer, BuildMinimumSequenceIdentityString


class BuildStreamlitMainPage:
    def __call__(self):
        st.set_page_config(layout="wide")

        values = [
            0.995,
            0.996,
            0.997,
            0.998,
            0.999,
            0.9995,
            0.9996,
            0.9997,
            0.9998,
            0.9999,
        ]

        minimum_sequence_identity = st.select_slider(
            label="Minimum identity to cluster",
            key="minimum_sequence_identity",
            options=[
                "99.5%",
                "99.6%",
                "99.7%",
                "99.8%",
                "99.9%",
                "99.95%",
                "99.96%",
                "99.97%",
                "99.98%",
                "99.99%",
            ],
            value="99.5%",
            help="To be the same cluster (color), how similar do two androgen receptors need to be?",
        )
        # st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
        st.pydeck_chart(
            BuildDeckRenderer()(
                BuildMinimumSequenceIdentityString()(minimum_sequence_identity)
            )
        )


BuildStreamlitMainPage()()
