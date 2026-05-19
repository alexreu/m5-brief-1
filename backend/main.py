from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel, StrictInt

from modules.calcul import calcul


app = FastAPI(title="API Calcul", version="1.0.0")


class CalculRequest(BaseModel):
    nombre: StrictInt


class CalculResponse(BaseModel):
    nombre: int
    resultat: int


@app.get("/")
def read_root() -> dict[str, str]:
    logger.info("Route / appelee")
    return {"message": "Bienvenue sur l'API de calcul"}


@app.get("/health")
def health_check() -> dict[str, str]:
    logger.info("Route /health appelee")
    return {"status": "ok"}


@app.post("/calcul", response_model=CalculResponse)
def calculate_square(payload: CalculRequest) -> CalculResponse:
    logger.info("Calcul du carre pour nombre={}", payload.nombre)
    resultat = calcul(payload.nombre)
    return CalculResponse(nombre=payload.nombre, resultat=resultat)
