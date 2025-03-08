from datetime import datetime
from typing import List
from fastapi import APIRouter

from app.models.car import CarRegister
from app.log.logger import logger

router = APIRouter()
car_register = CarRegister()


@router.get("/", response_model=List[str])
def get_cars():
    try:
        return car_register.get_cars()
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se consultaron todos los automoviles",
        })
