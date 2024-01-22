import streamlit as st
import requests
import json

def main_page():

  name = st.text_input("Ingresa tu nombre")
  mail = st.text_input("Ingresa tu correo")

  if st.button('Enviar información'):
     
      # Definir endpoint
      # url = 'https://4507-38-43-130-92.ngrok-free.app/users'

      # Definir la data que se enviará a la API
      data = {"name": name, 
              "email": mail}

      # Parámetros adicionales enviados con la solicitud
      headers = {"Content-Type": "application/json"}

      # Obtener respuesta a solicitud
      response = requests.post(url, 
                              data=json.dumps(data), 
                              headers=headers)

      # Obtener e imprimir de respuesta
      st.text(response.json()["message"])

# Punto de entrada de la aplicación Streamlit
if __name__ == "__main__":
    main_page()