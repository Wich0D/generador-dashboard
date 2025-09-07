import os.path

import streamlit as st
from PIL import Image


# Imagenes
image_path = os.path.join('images', 'guide_1.png')
image1 = Image.open(image_path)
image_path = os.path.join('images', 'guide_2.png')
image2 = Image.open(image_path)
image_path = os.path.join('images', 'guide_3.png')
image3 = Image.open(image_path)

text = "SIIfkafa"
st.title("📊 Guia de uso")

st.text("Para poder generar tu dashboard necesitas simplemente seguir los siguientes pasos")

st.markdown(f"""            
#### 1. Prepara tu hoja de calculo y subela

Para poder iniciar necesitas una **hoja de calculo** en formato **.xlsx** o **.csv**.Debe seguir el siguiente formato:

- Todos los datos de una columna deben ser de un mismo tipo: 
    - Numericos: Solamente utilizar valores numericos en los registros (0 - 9), evita utilizar unidades
    - Fecha: Respeta cualquiera de llos siguientes formatos
    - Texto (String): En este tipo de dato no tiene restricciones de nomenclatura
    - Booleano: Solo pueden tener dos valores, True o False        
- El archivo no debe pesar mas de 200 MB, en caso contrario no lo podra procesar el sitema
- **No utilices filas como columnas**, en este caso el programa no podrá trabajar con tus datos.    

Una vez tus datos cumplan con el formato establecido, entra a la página **Generar Dashboard** y arrastra o selecciona tu archivo en el dropbox:
""")
st.image(image1, caption="Dropbox en página Generar Dashboard")
st.page_link(r"app_pages\main_page.py", label="Generar Dashboard", icon="✏️")
st.markdown(f"""  
---          
#### 2. Asegurate que los tipos de datos sean correctos
            
Una vez que cargaste el archivo, podras observar una vista previa de tus datos y una tabla donde puedes ajustar el tipo de dato de las columnas y reajustar su nombre
para poder hacer un analisis mas preciso
""")
st.image(image2, caption="Tabla para renombrar columnas y cambiar tipo de dato")
st.markdown(f"""  
> **Nota: Asegurate de colocar los tipos de datos correctos, de lo contrario el analisis puede ser poco preciso**
""")
st.markdown(f""" 
---
#### 3. Genera tus graficos y guardalos

Comienza a seleccinar los parametros en la seccion **Genera una gáfica. Asigna un nombre a tu gráfica, el tipo de gráfica y por último los valores que se van a analizar:
""")

st.markdown(f""" 
Una vez que termines de seleccionar los parámetros da click en el botón **💾 Guardar grafica en Dashboard** para agregar la gráfica a tu dashboard final, debe aparecer el siguiente mensaje de confirmación:                       
""")
st.image(image3, caption="Formulario para generar la gráfica")
st.markdown(f""" 
---
#### 4. Observa tu resultado y descargalo
Accede a la pagina **Dashboard Final** y podras observar un listado de todas las gráficas que ya has guardado anteriormente, podras eliminar aquellas que no deseas conservar
con el boton **❌ Eliminar gráfica**, en caso de que tengas ya todos los resultados que deseas, da click en el boton **Descargar** e iniciara la descarga de tu dashboard en formato HTML y PDF.                                   
""")
st.page_link(r"app_pages\main_page.py", label="Acceder a Dashboard Final", icon="📊")

