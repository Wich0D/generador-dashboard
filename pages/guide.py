import streamlit as st

st.title("📊 Guia de uso")

st.text("Para poder generar tu dashboard necesitas simplemente seguir los siguientes pasos")

st.markdown("""            
#### 1. Prepara tu hoja de calculo y subela

Para poder iniciar necesitas una **hoja de calculo** en formato **.xlsx** o **.csv**.Debe seguir el siguiente formato:

- Todos los datos de una columna deben ser de un mismo tipo: 
    - Numericos: Solamente utilizar valores numericos en los registros (0 - 9), evita utilizar unidades
    - Fecha: Respeta cualquiera de llos siguientes formatos
    - Texto (String): En este tipo de dato no tiene restricciones de nomenclatura
    - Booleano: Solo pueden tener dos valores, True o False        
- El archivo no debe pesar mas de 200 MB, en caso contrario no lo podra procesar el sitema
- **No utilices filas comoo columnas**, en este caso el programa no podra trabajar tus datos.    

Una vez tus datos cumplan con el formato establecido, entra a la pagina principal y arrastra o selecciona tu archivo:
           
#### 2. Asegurate que los tipos de datos sean correctos
            
Una vez que cargaste el archivo, podras observar una vista previa de tus datos y una tabla donde puedes ajustar el tipo de dato de las columnas y reajustar su nombre
para poder hacer un analisis mas preciso

> ** Nota: Asegurate de colocar los tipos de datos correctos, de lo contrario el analisis puede ser poco preciso  **
             
#### 3. Genera tus graficos y guardalos

Comienza a seleccinar los parametros en la seccion **Generar grafica**, asigna un nombre a tu grafica, el tipo de grafica y por ultimo los valores que se van a analizar.
Una vez que termines de seleccionar los parametros da clic en el boton **Guardar** para agregar la grafica a tu dashboard final, debe aarecer el siguiente mensaje de confirmacion:                       

#### 4. Observa tu resultado y descargalo
Accede a la pagina **Dashboard Final** y podras observar un listado de todas las graficas que ya has guardado anteriormente, podras eliminar aqullas que no deseas conservar
con el boton **eliminar**, en caso de que tengas ya todos los resultados que deseas, da click en el boton **Descargar** e iniciara la descarga de tu dashboard en formato HTML y PDF.                                   
""")
