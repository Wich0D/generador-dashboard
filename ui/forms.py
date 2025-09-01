import streamlit as st
import pandas as pd
import plotly.express as px

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
                index=("numeric", "string", "boolean", "datetime").index(default_type)
            )

            new_types[column] = selected_type

        submitted = st.form_submit_button("Guardar tipos")

    if submitted:
        return new_types
    return None


def chart_columns_type_selector(df, data_type, chart_type):
    """Formulario para elegir columnas según el tipo de gráfico"""

    # Filtrar columnas por tipo
    numeric_cols = [col for col, t in data_type.items() if t == "numeric"]
    datetime_cols = [col for col, t in data_type.items() if t == "datetime"]
    string_cols = [col for col, t in data_type.items() if t == "string"]

    fig = None  # Inicializamos fig
    chart_name = st.text_input("Nombre de la gráfica", value= "")

    if chart_type == "Línea":
        x = st.selectbox("Eje X (fecha)", datetime_cols)
        y = st.selectbox("Eje Y (valor)", numeric_cols)
        fig = px.line(df, x=x, y=y)

    elif chart_type == "Barras":
        x = st.selectbox("Categoría", string_cols)
        y = st.selectbox("Valor", numeric_cols)
        fig = px.bar(df, x=x, y=y)

    elif chart_type == "Pie":
        names = st.selectbox("Categoría", string_cols)
        values = st.selectbox("Valores", numeric_cols)
        fig = px.pie(df, names=names, values=values)

    elif chart_type == "Dispersión":
        x = st.selectbox("Eje X", numeric_cols)
        y = st.selectbox("Eje Y", numeric_cols)
        fig = px.scatter(df, x=x, y=y)
    return fig,chart_name



