import streamlit as st
import pandas as pd
import numpy as np

file = 'data\Twitch_game_data.csv'
data = pd.read_csv(file, encoding='latin-1')

st.set_page_config(layout="wide")

st.title('Projeto MetaVerso')
st.sidebar.write("barra lateral")
