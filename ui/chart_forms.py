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
    return fig

def pie_chart_form(df):
    """Gráfica de Pastel"""
    values = st.selectbox("Valores ", df.columns)
    if values:
        value_counter = df[values].value_counts()
        fig = px.pie(
            value_counter,
            names=value_counter.index,
            values=value_counter.values,
        )
        return fig
    else:
        return None

def ecdf_plot_form(df,numeric_cols):
    """Grafíca ECDF"""
    values = st.selectbox("Valores (númericos)", numeric_cols)
    fig = px.ecdf(
        df,
        x= values
    )
    fig.update_layout(
        xaxis_title=values,
        yaxis_title="Proporción Acumulada"
    )
    return fig

def chart_columns_type_selector(df, data_type, chart_type):
    """Formulario para elegir columnas según el tipo de gráfico"""

    # Filtrar columnas por tipo
    numeric_cols, datetime_cols, string_cols = type_filter(data_type)

    fig = None  # Inicializamos fig
    chart_name = st.text_input("Nombre de la gráfica", value= "")

    if chart_type == "Línea":
        x = st.selectbox("Eje X ", df.columns)
        y = st.selectbox("Eje Y ", df.columns)
        fig = px.line(df, x=x, y=y)

    elif chart_type == "Línea (múltiples)":
        fig = plotly_chart_form(df, data_type)

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

    elif chart_type == "Pie (Pastel)":
        fig = pie_chart_form(df)

    elif chart_type == "Dispersión":
        x = st.selectbox("Eje X", df.columns)
        y = st.selectbox("Eje Y", df.columns)
        fig = px.scatter(df, x=x, y=y)
    elif chart_type == "ECDF":
        fig = ecdf_plot_form(df, numeric_cols)

    return fig,chart_name