import streamlit as st
import pandas as pd
import plotly.express as px

from data.cleaner import clean_columns
from data.loader import load_data
from data.type_handler import detect_column_types
from ui.forms import column_selector

st.set_page_config(
    page_title= "Generador de Dashboards",
    page_icon="📊",
    layout="centered",
)
st.title("📊 Generador de Dashboards")

# Cargar archivo
uploaded_file = st.file_uploader("Sube tu archivo Excel o CSV", type=["xlsx", "csv"])

if uploaded_file:
    # Leer archivo
    df = load_data(uploaded_file)
    df = clean_columns(df)
    st.toast("Dataframe cargado con éxito", icon="😍")
    st.subheader("Vista previa de los datos:")
    st.dataframe(df.head(10))

    # Formulario de selector decolumnas
    selected_columns = column_selector(df)
    column_filter = selected_columns.loc[selected_columns['utilizar'] == True, 'columna']
    df_formatted = df[column_filter]

    # Configuración de columnas seleccionadas
    if df_formatted.empty or len(df_formatted.columns)<2:
        st.subheader("Debes seleccionar por lo menos dos columnas")
    else:
        st.subheader("Ajusta los datos para mayor precisión:")
        types = detect_column_types(df_formatted)
