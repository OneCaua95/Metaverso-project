import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
from extract import Extractor

data = Extractor()

def AnaliseDeSentimento():
    st.title('Projeto MetaVerso')
    st.sidebar.selectbox("barra lateral",("1","2"))

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.header("Garfico de Serntimento")
        df = data.get_data()
        st.bar_chart(df, x="Avg_viewer_ratio",y="Streamers")
    with col2:
        st.header("Top Comentarios")


    with col3:
        st.header("Usuarios Que mais Participam")

    with col4:
        st.header("Nuvem de Palavras")
    return

AnaliseDeSentimento()