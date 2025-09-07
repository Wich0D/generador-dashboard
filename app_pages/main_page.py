import time

import streamlit as st
from streamlit import session_state

from data.cleaner import clean_columns
from data.loader import load_data
from data.type_handler import detect_column_types, parse_columns
from ui.chart_forms import chart_columns_type_selector
from ui.dashboards import gen_chart
from ui.forms import *

st.set_page_config(
    page_title= "Generador de Dashboards",
    page_icon="📊",
    layout="centered",
)

chart_options = [
    "Línea",
    "Línea (múltiples)",
    "Barras",
    "Barras divididas",
    "Pie (Pastel)",
    "Dispersión",
    "ECDF"
]


def load_main_page(df):


    st.subheader("Vista previa de los datos:")
    st.dataframe(df.head(10))

    # Seleccion de tipos de datos

    types = detect_column_types(df)
    st.subheader("Reajusta tus columnas")
    new_columns_values = column_editor(df, types)

    if not new_columns_values.empty:
        if st.button("Guardar"):
            # Mapear columnas originales → nuevas
            rename_map = {
                old: new
                for old, new in zip(df.columns, new_columns_values["columna"].values)
                if old != new
            }

            if rename_map:
                st.session_state["df"].rename(columns=rename_map, inplace=True)
                st.toast("Cambios guardados ✅")
                time.sleep(1)
                st.rerun()

        


    # Formulario tipo de gráficas
    st.subheader("Genera una gráfica")

    # Inicializar lista de gráficas guardadas
    if "graficas_guardadas" not in st.session_state:
        st.session_state["graficas_guardadas"] = []


    chart_type = st.selectbox(
        "Selecciona el tipo de gráfica",
        chart_options
    )
    st.markdown("----")


    # Formulario de selector decolumnas
    data_type = detect_column_types(df)
    fig,chart_name = chart_columns_type_selector(df, data_type, chart_type)
    gen_chart(fig,chart_name)

    # Botón para guardar la gráfica
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])


    with col2:
        if st.button("💾 Guardar gráfica en dashboard"):
            st.session_state["graficas_guardadas"].append({
                "fig": fig,
                "name": chart_name
            })
            st.success("Gráfica añadida al Dashboard ✅")



# Load page
st.title("📊 Generador de Dashboards")

if "df" in st.session_state:
    df = st.session_state["df"]
    # Boton para volver a cargar archivo
    if "df" in st.session_state:
        reset_btn = st.button("Volver a elegir archivo")
        if reset_btn:
            del st.session_state["df"]
            st.rerun()
    # Cargar resto de la página
    load_main_page(df)
else:
    # Cargar archivo
    uploaded_file = st.file_uploader("Sube tu archivo Excel o CSV", type=["xlsx", "csv"])
    if uploaded_file:
        # Leer archivo
        df = load_data(uploaded_file)
        df = clean_columns(df)
        st.session_state["df"] = df
        load_main_page(df)
