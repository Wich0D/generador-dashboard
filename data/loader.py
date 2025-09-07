import pandas as pd

def load_data(file):
    """Carga CSV o Excel en un DataFrame"""
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        return pd.read_excel(file)
    else:
        raise ValueError("Formato no soportado. Usa CSV o Excel.")

def load_css():
    """Plantilla css predeterminada"""
    css_style = """
    <style>
        /* --- Fuentes de Google (Opcional, pero recomendado para mayor fidelidad) --- */
        @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&family=Source+Code+Pro&display=swap');

        /* --- Variables de Color (Tema Claro de Streamlit) --- */
        :root {
            --primary-color: #FF4B4B;
            --background-color: #F0F2F6;
            --secondary-background-color: #FFFFFF;
            --text-color: #31333F;
            --font: "open-sans";
            --code-font: "Source Code Pro", Menlo, Monaco, Consolas, "Courier New", monospace;
            --border-radius: 0.5rem;
        }

        /* --- Estilos Globales --- */
        body {
            font-family: var(--font);
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
            margin: 0;
            padding: 2rem;
        }

        /* --- Contenedor Principal (Simula el área de contenido) --- */
        .main-container {
            max-width: 800px;
            margin: auto;
            background-color: var(--secondary-background-color);
            padding: 2rem;
            border-radius: var(--border-radius);
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }

        /* --- Tipografía --- */
        h1, h2, h3 {
            font-weight: 700;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }

        h1 { font-size: 2.25rem; }
        h2 { font-size: 1.75rem; }
        h3 { font-size: 1.25rem; }
        p { margin-bottom: 1rem; }
        a { color: var(--primary-color); }
    </style>
"""
    return css_style