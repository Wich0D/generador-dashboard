import streamlit as st
import pandas as pd
import plotly.express as px


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
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Vista previa de los datos:")
    st.dataframe(df.head(5))



