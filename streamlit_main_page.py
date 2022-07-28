import streamlit as st
import pandas as pd
import numpy as np

from src.pydeck.arc_layer import build_deck_renderer

st.set_page_config(layout="wide")
st.pydeck_chart(build_deck_renderer(0.995))
