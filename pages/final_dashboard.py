import time

import streamlit as st

st.title("📊 Dashboard Final")

if "graficas_guardadas" not in st.session_state:
    st.session_state["graficas_guardadas"] = []

if st.session_state["graficas_guardadas"]:
    for i, g in enumerate(st.session_state["graficas_guardadas"]):
        st.subheader(g["name"] if g["name"] else f"Gráfica {i + 1}")
        st.plotly_chart(g["fig"], use_container_width=True)

        # Botón para eliminar
        if st.button("❌ Eliminar gráfica"):
            st.session_state["graficas_guardadas"].pop(i)
            st.toast("Página eliminada ",icon="❌")
            time.sleep(0.5)
            st.rerun()
else:
    st.info("Aún no has guardado gráficas.")