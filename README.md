# Generador de dashboard
Este proyecto es un generador automatizado de dashboards que ayuda a cualquiera a poder visualizar estadísticas de sus bases de datos sin necesidad de programar

## Requerimientos
- Instalar python en tu computadora, versión *3.12.3 o superior.* 
- Tener un navegador instalado como Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, y Opera. Preferentemenete en sus versiones más recientes
## Instalación de dependecias
Para la instalación de dependencias utiliza el siguiente comando en consola:
```bash
  pip install -r requirements.txt
```
## Inicio de servidor
1. Ejecuta el siguiente comando en consola para iniciar la aplicación
```bash
    streamlit run main.py
```
2. Abre la página en la URL [http://localhost:8501/](http://localhost:8501/)

## Estructura del proyecto 

```
📂 dashboard-generator
 ┣ 📂 app               # Código de la aplicación
 ┃ ┣ main.py            # Punto de entrada (Streamlit/Dash)
 ┃ ┣ utils.py           # Funciones auxiliares (lectura de Excel, limpieza, etc.)
 ┃ ┗ charts.py          # Funciones de generación de gráficos
 ┣ 📂 data              # Archivos de prueba
 ┣ requirements.txt     # Dependencias (pandas, streamlit, plotly, etc.)
 ┗ README.md            # Documentación
```

