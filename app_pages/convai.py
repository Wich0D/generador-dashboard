import streamlit as st
import requests, json
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()




# --- Configuración de la API de Convai ---
CONVAI_API_KEY = os.getenv("CONVAI_API_KEY")

CHARACTER_ID = "d5e892a8-8d31-11f0-a423-42010a7be01f"  # Reemplaza con el ID de tu personaje
API_URL = f"https://api.convai.com/character/getResponse"
# Comentar en caso de que quieras probar localmente
CONVAI_API_KEY = st.secrets["CONVAI_API_KEY"]

# --- Interfaz de Usuario con Streamlit ---
st.title("🤖 Databot")
st.caption("Conoce a nuestro asistente virtual")

# --- Gestión del Historial de Chat y Session ID ---
# Inicializa el historial de mensajes si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Inicializa un session id base
if "session_id" not in st.session_state:
    st.session_state.session_id = '-1'

# --- Mostrar Mensajes del Historial ---
# Muestra los mensajes guardados en cada recarga de la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Función para Interactuar con la API de Convai ---
def get_convai_response(user_message, session_id):
    headers = {
        "CONVAI-API-KEY": CONVAI_API_KEY,
        # "Content-Type": "application/json"
    }
    payload = {
        "userText": user_message,
        "charID": CHARACTER_ID,
        "sessionID": session_id,
        "text": user_message
    }
    try:
        response = requests.request("POST", API_URL, headers=headers, data=payload)
        data = response.json()
        if session_id == '-1':
            st.session_state.session_id = data['sessionID']
        texto_de_respuesta = data['text']
        return texto_de_respuesta
    except requests.exceptions.RequestException as e:
        st.error(f"Error al conectar con la API de Convai: {e}")
        return "Error de conexión."

# --- Entrada del Usuario y Lógica Principal ---
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Añadir mensaje del usuario al historial y mostrarlo
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtener y mostrar la respuesta del chatbot
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Pensando..."):
            bot_response = get_convai_response(prompt, st.session_state.session_id)
            message_placeholder.markdown(bot_response)

    # Añadir respuesta del chatbot al historial
    st.session_state.messages.append({"role": "assistant", "content": bot_response})