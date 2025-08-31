import streamlit as st
import pandas as pd


def column_selector(df):
    """Formulario para elegir las columnas a analizar"""
    st.subheader("Elige y renombra las columnas a considerar")

    # Crear DataFrame temporal para el editor
    data_selector = pd.DataFrame({
        "columna": df.columns,
        "utilizar": [False] * len(df.columns),
    })

    # Mostrar editor interactivo
    selected_columns = st.data_editor(
        data_selector,
        column_config={
            "columna": st.column_config.TextColumn(
                "Columna",
                help="Renombra la columna para tu dashboard si así lo deseas"
            ),
            "utilizar": st.column_config.CheckboxColumn(
                "Incluir en Dashboard",
                help="Selecciona la columna que desea analizar",
                default=False
            )
        },
        hide_index=True
    )
    return selected_columns


def columns_type_selector(df):
    """Formulario para elegir especificaciones de columnas"""
    st.subheader("Ajusta las configuraciones de columnas")



