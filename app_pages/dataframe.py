import streamlit as st

st.set_page_config(
    layout="wide"
)
st.title("Dataframe")

if "df" in st.session_state:
    df = st.session_state["df"]
    st.dataframe(df,height="auto")
else:
    st.info("No se ha cargado ningún archivo todavía.")