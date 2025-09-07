import streamlit as st
import pandas as pd
import plotly.express as px

from ui.chart_forms import plotly_chart_form


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


def columns_type_selector(df, data_type):
    """Formulario para elegir especificaciones de columnas"""
    new_types = {}

    with st.form("columns_type_form"):
        st.write("Configura el tipo de cada columna si es necesario")

        for column in df.columns:
            # Valor por defecto: el que ya está en data_type, si existe
            default_type = data_type.get(column, "string")

            selected_type = st.selectbox(
                f"{column}",
                ("numeric", "string", "boolean", "datetime"),
                index=("numeric", "string", "datetime").index(default_type)
            )

            new_types[column] = selected_type

        submitted = st.form_submit_button("Guardar tipos")

    if submitted:
        st.success("Tipo de datos guardados correctamente ✅")
        return new_types
    return None

def column_editor(df,data_type):
    """Formulario para renombrar y ajustar tipo de columnas"""
    st.subheader("Elige y renombra las columnas a considerar")

    # Crear DataFrame temporal para el editor
    data_selector = pd.DataFrame({
        "columna": df.columns,
        "tipo": list(data_type.values()),
    })

    # Mostrar editor interactivo
    selected_columns = st.data_editor(
        data_selector,
        column_config={
            "columna": st.column_config.TextColumn(
                "Columna",
                help="Renombra la columna para tu dashboard si así lo deseas"
            ),
            "tipo": st.column_config.SelectboxColumn(
                "Tipo de dato",
                help="Selecciona el tipo de columna",
                options=["numeric", "string","datetime"],
            )
        },
        hide_index=True,
        key="Column_editor"
    )

    return selected_columns




