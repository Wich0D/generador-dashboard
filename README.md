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
    streamlit run app.py
```
2. Abre la página en la URL [http://localhost:8501/](http://localhost:8501/)
3. Cierra el servidor local en consola con el comando `ctrl + c` en windows.

## Estructura del proyecto 

```
project/
│── app.py                  # archivo principal (Streamlit)
│── data/
│   ├── loader.py           # funciones para leer datos
│   ├── cleaner.py          # funciones para limpiar y normalizar
│   ├── type_handler.py     # funciones para tratamiento tipos de columna
│── ui/
│   ├── forms.py            # formularios de selección de columnas
│   ├── dashboards.py       # vistas de gráficos
│── utils/
│   ├── config.py           # manejo de configuración (JSON, etc.)
│   ├── helpers.py          # funciones auxiliares

```

