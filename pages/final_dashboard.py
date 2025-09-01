import time
import io
import streamlit as st

st.title("📊 Dashboard Final")

if "graficas_guardadas" not in st.session_state:
    st.session_state["graficas_guardadas"] = []

if st.session_state["graficas_guardadas"]:
    for i, g in enumerate(st.session_state["graficas_guardadas"]):
        st.subheader(g["name"] if g["name"] else f"Gráfica {i + 1}")
        st.plotly_chart(g["fig"], use_container_width=True)

        # Botón para eliminar
        if st.button("❌ Eliminar gráfica", key=f"eliminar_{i}"):
            st.session_state["graficas_guardadas"].pop(i)
            st.toast("Página eliminada ",icon="❌")
            time.sleep(0.5)
            st.rerun()

    graficas = st.session_state.get("graficas_guardadas", [])
    # Botón único para descargar  como HTML
    if st.button("📥 Descargar dashboard completo"):
        buf = io.StringIO()
        html_sections = []

        html_sections.append(f"<h1>{st.session_state.get('dashboard_title', 'Dashboard Final')}</h1>")

        for i, g in enumerate(graficas):
            title = g["name"] if g["name"] else f"Gráfica {i + 1}"
            subtitle = g.get("subtitle", "")  # si quieres permitir subtítulos
            # Título y subtítulo como HTML
            html_section = f"<h2>{title}</h2>"
            if subtitle:
                html_section += f"<h4>{subtitle}</h4>"
            # Insertamos la gráfica
            html_section += g["fig"].to_html(full_html=False, include_plotlyjs="cdn")
            html_sections.append(html_section)

        html_content = "<html><body>" + "".join(html_sections) + "</body></html>"
        buf.write(html_content)
        buf.seek(0)

        st.download_button(
            label="Descargar dashboard HTML",
            data=buf.getvalue(),
            file_name="dashboard_final.html",
            mime="text/html"
        )
else:
    st.info("Aún no has guardado gráficas.")


