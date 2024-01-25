# Importar las bibliotecas necesarias
import streamlit as st
import requests
import json

def main_page():
  # Crear un título para la página principal
  st.title("Formulario de registro")

  # Crear campos de entrada de texto para el nombre y el correo electrónico
  name = st.text_input("Ingresa tu nombre")  # Recoger el nombre del usuario
  mail = st.text_input("Ingresa tu correo")  # Recoger el correo electrónico del usuario

  # Crear un botón para enviar la información
  if st.button('Enviar información'):
     
      # Definir la URL del endpoint de la API
      url = 'https://0d8e-38-43-130-92.ngrok-free.app/users'

      # Crear un diccionario con los datos a enviar a la API
      data = {"name": name, 
              "email": mail}

      # Definir los encabezados de la solicitud
      headers = {"Content-Type": "application/json"}

      # Enviar la solicitud POST a la API
      response = requests.post(url, 
                              data=json.dumps(data), 
                              headers=headers)

      # Obtener el mensaje de la respuesta y mostrarlo en la aplicación
      st.text(response.json()["message"])

# Punto de entrada principal de la aplicación Streamlit
if __name__ == "__main__":
    main_page()