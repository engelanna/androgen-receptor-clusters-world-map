import streamlit as st
import pandas as pd
import numpy as np

from src.builders import (
    BuildDeckRenderer,
    BuildLegend,
    BuildMinimumSequenceIdentityString,
)


class BuildStreamlitMainPage:
    def __call__(self):
        st.set_page_config(layout="wide")

        st.subheader(
            "[Androgen receptor clusters - world map (4654 genomes)](https://github.com/engelanna/androgen-receptor-clustering)",
        )

        minimum_sequence_identity = st.selectbox(
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
            help="To be the same cluster (color), how similar do two androgen receptors need to be?",
        )
        st.pydeck_chart(
            BuildDeckRenderer()(
                BuildMinimumSequenceIdentityString()(minimum_sequence_identity)
            )
        )
        BuildLegend()()

        st.text("")
        st.text("")
        st.text(
            "#trivium On average, 2 random Africans are more genetically diverse, "
            "than 2 random people picked from anywhere in the whole world."
        )
        st.text(
            "#caveat That being said, don't trust the Gambia data too much, "
            """it was awfully low coverage."""
        )


BuildStreamlitMainPage()()
