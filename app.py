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


pages = [
        st.Page("app_pages/main_page.py", title="Generar Dashboard", icon="✏️"),
        st.Page("app_pages/dataframe.py", title="Ver Dataframe", icon="📋"),
        st.Page("app_pages/final_dashboard.py", title="Dashboard Final", icon="📊"),
        st.Page("app_pages/guide.py", title="Guia rapida", icon="📓"),
        st.Page("app_pages/pruebas.py", title="Prueba", icon="📓")
    ]
pg = st.navigation(pages, position="sidebar",expanded=True)
pg.run()