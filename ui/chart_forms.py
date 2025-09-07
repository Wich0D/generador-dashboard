import streamlit as st
import pandas as pd
import plotly.express as px

def type_filter(data_type):
    """Filtrar tipo de datos"""
    # Filtrar columnas por tipo
    numeric_cols = [col for col, t in data_type.items() if t == "numeric"]
    datetime_cols = [col for col, t in data_type.items() if t == "datetime"]
    string_cols = [col for col, t in data_type.items() if t == "string"]

    return numeric_cols, datetime_cols, string_cols

def plotly_chart_form(df,data_type):
    """Gráfica de líneas comparativas"""
    numeric_cols, datetime_cols, string_cols = type_filter(data_type)
    # Seleccionar columna
    x = st.selectbox("Eje X (fecha)", df.columns)
    y = st.selectbox("Eje Y (valor)", df.columns)
    color = st.selectbox("Tipo de datos", df.columns)
    fig = px.line(df, x=x, y=y,color=color)
    st.plotly_chart(fig, use_container_width=True)
    return fig

def pie_chart_form(df,data_type):
    st.number_input("Cantidad de datos a comparar")

def chart_columns_type_selector(df, data_type, chart_type):
    """Formulario para elegir columnas según el tipo de gráfico"""

    # Filtrar columnas por tipo
    numeric_cols = [col for col, t in data_type.items() if t == "numeric"]
    datetime_cols = [col for col, t in data_type.items() if t == "datetime"]
    string_cols = [col for col, t in data_type.items() if t == "string"]

    fig = None  # Inicializamos fig
    chart_name = st.text_input("Nombre de la gráfica", value= "")

    if chart_type == "Línea":
        x = st.selectbox("Eje X (fecha)", df.columns)
        y = st.selectbox("Eje Y (valor)", df.columns)
        fig = px.line(df, x=x, y=y)

    elif chart_type == "Línea (múltiples)":
        plotly_chart_form(df, data_type)

    elif chart_type == "Barras":
        x = st.selectbox("Categoría", df.columns)
        y = st.selectbox("Valor", df.columns)
        fig = px.bar(df, x=x, y=y)
    elif chart_type == "Barras divididas":
        x = st.selectbox("Categoría", df.columns)
        y = st.selectbox("Valor", df.columns)
        color = st.selectbox("Tipo de datos", df.columns)
        bar_type = st.checkbox("Agrupar barras")
        if bar_type:
            fig = px.bar(df, x=x, y=y, color=color, barmode="group")
        else:
            fig = px.bar(df, x=x, y=y, color=color)

    elif chart_type == "Pie":
        names = st.selectbox("Categoría", df.columns)
        values = st.selectbox("Valores", df.columns)
        fig = px.pie(df, names=names, values=values)

    elif chart_type == "Dispersión":
        x = st.selectbox("Eje X", df.columns)
        y = st.selectbox("Eje Y", df.columns)
        fig = px.scatter(df, x=x, y=y)
    return fig,chart_name