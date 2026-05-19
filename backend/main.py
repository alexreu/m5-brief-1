from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel, StrictInt

from modules.calcul import calcul


app = FastAPI(title="Square Calculation API", version="1.0.0")


class CalculRequest(BaseModel):
    number: StrictInt


class CalculResponse(BaseModel):
    number: int
    result: int


@app.get("/")
def read_root() -> dict[str, str]:
    logger.info("Route / called")
    return {"message": "Welcome to the square calculation API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    logger.info("Route /health called")
    return {"status": "ok"}


@app.post("/calcul", response_model=CalculResponse)
def calculate_square(payload: CalculRequest) -> CalculResponse:
    logger.info("Calculating square for number={}", payload.number)
    result = calcul(payload.number)
    return CalculResponse(number=payload.number, result=result)
