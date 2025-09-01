import streamlit as st
import pandas as pd
import plotly.express as px

from data.cleaner import clean_columns
from data.loader import load_data
from data.type_handler import detect_column_types
from ui.forms import column_selector, columns_type_selector

st.set_page_config(
    page_title= "Generador de Dashboards",
    page_icon="📊",
    layout="centered",
)

pages ={
    "Menu": [
        st.Page(r"pages\main_page.py", title="Generar Dashboard"),
        st.Page(r"pages\dataframe.py", title="Ver Dataframe"),
        st.Page(r"pages\final_dashboard.py", title="Dashboard Final"),
    ]
}
pg = st.navigation(pages)
pg.run()

