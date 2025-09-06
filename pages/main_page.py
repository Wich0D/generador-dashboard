import streamlit as st

from data.cleaner import clean_columns
from data.loader import load_data
from data.type_handler import detect_column_types
from ui.dashboards import gen_chart
from ui.forms import *

st.set_page_config(
    page_title= "Generador de Dashboards",
    page_icon="📊",
    layout="centered",
)
# Cargar datos si ya se eligió un archivo
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None
if "df" not in st.session_state:
    st.session_state["df"] = None

st.title("📊 Generador de Dashboards")

# Cargar archivo
uploaded_file = st.file_uploader("Sube tu archivo Excel o CSV", type=["xlsx", "csv"])

if uploaded_file:
    # Leer archivo
    df = load_data(uploaded_file)
    df = clean_columns(df)
    st.session_state["df"] = df
    #st.toast("Dataframe cargado con éxito", icon="😍")
    st.subheader("Vista previa de los datos:")
    st.dataframe(df.head(10))

    # Seleccion de tipos de datos
    #st.subheader("Ajusta los datos para mayor precisión:")
    types = detect_column_types(df)
    #columns_type_selector(df, types)
    st.subheader("Reajusta tus columnas")
    new_df = column_editor(df,types)
    if not new_df.empty:
        if st.button("Guardar"):
            new_df = new_df.copy()
            print(new_df)
            st.toast("Cambios guardados")
        


    # Formulario tipo de gráficas
    st.subheader("Genera una gráfica")

    # Inicializar lista de gráficas guardadas
    if "graficas_guardadas" not in st.session_state:
        st.session_state["graficas_guardadas"] = []

    chart_type = st.selectbox(
        "Selecciona el tipo de gráfica",
        ["Línea", "Barras","Pie (Pastel)","Dispersión"]
    )
    st.markdown("----")
    # Formulario de selector decolumnas
    data_type = detect_column_types(df)
    fig,chart_name = chart_columns_type_selector(df, data_type, chart_type)
    gen_chart(fig,chart_name)

    # Botón para guardar la gráfica
    if st.button("💾 Guardar gráfica en dashboard"):
        st.session_state["graficas_guardadas"].append({
            "fig": fig,
            "name": chart_name
        })
        st.success("Gráfica añadida al Dashboard ✅")


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
        columns_type_selector(df_formatted, types)
