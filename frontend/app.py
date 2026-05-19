import os

import requests
import streamlit as st
from loguru import logger


BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


st.set_page_config(page_title="Calcul de carre", page_icon="2", layout="centered")

st.title("Calcul de carre")
st.write("Saisis un entier, puis envoie-le a l'API FastAPI pour obtenir son carre.")

nombre = st.number_input("Entier a calculer", value=0, step=1, format="%d")

if st.button("Calculer"):
    payload = {"nombre": int(nombre)}
    logger.info("Envoi de la requete vers {} avec payload={}", BACKEND_URL, payload)

    try:
        response = requests.post(f"{BACKEND_URL}/calcul", json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        logger.info("Reponse recue: {}", data)
        st.success(f"Le carre de {data['nombre']} est {data['resultat']}.")
    except requests.RequestException as exc:
        logger.error("Erreur lors de l'appel API: {}", exc)
        st.error("Impossible de joindre l'API backend.")
