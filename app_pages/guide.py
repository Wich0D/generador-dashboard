import os.path

import streamlit as st
from PIL import Image

# Imágenes
image_path = os.path.join('images', 'guide_1.png')
image1 = Image.open(image_path)
image_path = os.path.join('images', 'guide_2.png')
image2 = Image.open(image_path)
image_path = os.path.join('images', 'guide_3.png')
image3 = Image.open(image_path)

text = "SIIfkafa"
st.title("📊 Guía de uso")

st.text("Para poder generar tu dashboard, simplemente necesitas seguir los siguientes pasos.")

st.markdown(f"""            
#### 1. Prepara tu hoja de cálculo y súbela

Para poder iniciar, necesitas una **hoja de cálculo** en formato **.xlsx** o **.csv**. Debe seguir el siguiente formato:

- Todos los datos de una columna deben ser del mismo tipo: 
    - Numéricos: Solamente utilizar valores numéricos en los registros (0 - 9), evita utilizar unidades.
    - Fecha: Respeta cualquiera de los siguientes formatos.
    - Texto (String): Este tipo de dato no tiene restricciones de nomenclatura.
    - Booleano: Solo pueden tener dos valores: True o False.        
- El archivo no debe pesar más de 200 MB; en caso contrario, el sistema no lo podrá procesar.
- **No utilices filas como columnas**, en este caso, el programa no podrá trabajar con tus datos.    

Una vez que tus datos cumplan con el formato establecido, entra a la página **Generar Dashboard** y arrastra o selecciona tu archivo en el Dropbox:
""")
st.image(image1, caption="Dropbox en la página 'Generar Dashboard'")
st.page_link(r"app_pages/main_page.py", label="Generar Dashboard", icon="✏️")
st.markdown(f"""  
---          
#### 2. Asegúrate de que los tipos de datos sean correctos

Una vez que hayas cargado el archivo, podrás observar una vista previa de tus datos y una tabla donde puedes ajustar el tipo de dato de las columnas y reajustar su nombre
para poder hacer un análisis más preciso.
""")
st.image(image2, caption="Tabla para renombrar columnas y cambiar el tipo de dato")
st.markdown(f"""  
> **Nota: Asegúrate de colocar los tipos de datos correctos; de lo contrario, el análisis puede ser poco preciso.**
""")
st.markdown(f""" 
---
#### 3. Genera tus gráficos y guárdalos

Comienza a seleccionar los parámetros en la sección **Genera una gráfica**. Asigna un nombre a tu gráfica, el tipo de gráfica y, por último, los valores que se van a analizar:
""")

st.markdown(f""" 
Una vez que termines de seleccionar los parámetros, da clic en el botón **💾 Guardar gráfica en Dashboard** para agregar la gráfica a tu dashboard final. Debe aparecer el siguiente mensaje de confirmación:                       
""")
st.image(image3, caption="Formulario para generar la gráfica")
st.markdown(f""" 
---
#### 4. Observa tu resultado y descárgalo
Accede a la página **Dashboard Final** y podrás observar un listado de todas las gráficas que ya has guardado anteriormente. Podrás eliminar aquellas que no desees conservar
con el botón **❌ Eliminar gráfica**. En caso de que ya tengas todos los resultados que deseas, da clic en el botón **Descargar** e iniciará la descarga de tu dashboard en formato HTML.                                   
""")
st.page_link(r"app_pages/final_dashboard.py", label="Acceder al Dashboard Final", icon="📊")