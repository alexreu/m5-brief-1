import os

import requests
import streamlit as st
from loguru import logger


BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


st.set_page_config(page_title="Square Calculator", page_icon="2", layout="centered")

st.title("Square Calculator")
st.write("Enter an integer and send it to the FastAPI backend to get its square.")

number = st.number_input("Integer to calculate", value=0, step=1, format="%d")

if st.button("Calculate"):
    payload = {"number": int(number)}
    logger.info("Sending request to {} with payload={}", BACKEND_URL, payload)

    try:
        response = requests.post(f"{BACKEND_URL}/calcul", json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        logger.info("Response received: {}", data)
        st.success(f"The square of {data['number']} is {data['result']}.")
    except requests.RequestException as exc:
        logger.error("Error while calling the API: {}", exc)
        st.error("Unable to reach the backend API.")
