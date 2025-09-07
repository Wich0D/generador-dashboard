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

        # Usamos columnas para poner los botones en una sola línea
        col1, col2, col3 = st.columns([1, 1, 1])  # Columnas para botones y un espacio

        with col1:
            # Botón para subir: solo aparece si no es el primer elemento
            if i > 0:
                if st.button("🔼 Subir", key=f"subir_{i}", use_container_width=True):
                    # Intercambia el elemento actual con el anterior
                    (st.session_state["graficas_guardadas"][i], st.session_state["graficas_guardadas"][i - 1]) = \
                        (st.session_state["graficas_guardadas"][i - 1], st.session_state["graficas_guardadas"][i])
                    st.rerun()
            else:
                st.button("🔼 Subir", key=f"subir_{i}", use_container_width=True,disabled=True)
        with col2:
            # Botón para eliminar (como lo tenías)
            if st.button("❌ Eliminar", key=f"eliminar_{i}", use_container_width=True):
                st.session_state["graficas_guardadas"].pop(i)
                st.toast("Gráfica eliminada", icon="🗑️")
                st.rerun()

        with col3:
            # Botón para bajar: solo aparece si no es el último elemento
            if i < len(st.session_state["graficas_guardadas"]) - 1:
                if st.button("🔽 Bajar", key=f"bajar_{i}", use_container_width=True):
                    # Intercambia el elemento actual con el siguiente
                    (st.session_state["graficas_guardadas"][i], st.session_state["graficas_guardadas"][i + 1]) = \
                        (st.session_state["graficas_guardadas"][i + 1], st.session_state["graficas_guardadas"][i])
                    st.rerun()
            else:
                st.button("🔽 Bajar", key=f"bajar_{i}", use_container_width=True,disabled=True)


    # Botón único para descargar  como HTML
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        final_name = st.text_input("Elige el nombre de tu dashboard:")
        if final_name is None:
            final_name = "Dashboard"

    with col3:


        if st.button("📥 Descargar dashboard completo"):
            buf = io.StringIO()
            html_sections = []

            html_sections.append(f"<h1>{st.session_state.get('dashboard_title', final_name)}</h1>")
            graficas = st.session_state.get("graficas_guardadas", [])
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
                file_name=f"{final_name}.html",
                mime="text/html"
            )
else:
    st.info("Aún no has guardado gráficas.")


