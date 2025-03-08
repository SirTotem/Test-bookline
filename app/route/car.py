from datetime import datetime
from typing import List
from fastapi import APIRouter

from app.models.car import Car
from app.log.logger import logger
from app.route.register import car_register

router = APIRouter()


@router.get("/", response_model=List[str])
def get_cars():
    try:
        return car_register.get_cars()

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(),
            'level': "ERROR",
            'message': f"Error en consulta de automoviles: {e}",
        })
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se consultaron todos los automoviles",
        })

@router.put("/", response_model=str)
def create_car(license: str, color: str, brand: str):
    try:
        new_car = Car(license=license, color=color, brand=brand)
        car_register.add_car(new_car)
        return f"Se ha añadido al registro el coche {str(new_car)} de color {color}"

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(),
            'level': "ERROR",
            'message': f"Error en la creacion de automovil: {e}",
        })
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': f"Se creo el automovil {str(new_car)} correctamente",
        })



@router.delete("/", response_model=str)
def remove_car(license: str):
    try:
        car_register.delete_car(license)
        return f"Se ha eliminado al registro el coche {license}"
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': f"Se Elimino del registro el automovil {license}",
        })
