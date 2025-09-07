import streamlit as st
import plotly.express as px
import pandas as pd



def gen_chart(fig,name):
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True,key=f"grafica{len(st.session_state["graficas_guardadas"])}")
    else:
        st.markdown("> **Selecciona una columna valida**")