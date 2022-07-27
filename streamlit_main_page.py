import streamlit as st
import pandas as pd
import numpy as np

from src.pydeck.arc_layer import deck_renderer

st.pydeck_chart(deck_renderer)
