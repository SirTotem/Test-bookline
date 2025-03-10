from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException

from app.models.car import Car
from app.log.logger import logger
from app.db.register import car_register, save_to_database

router = APIRouter()


@router.get("/", response_model=List[str])
def get_cars():
    logger.info({
        'timestamp': datetime.now(), 'level': "INFO",
        'message': "Se ha iniciado la peticion para consultar los vehiculos",
    })
    try:
        result = car_register.get_cars()

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(), 'level': "ERROR",
            'message': f"No se completo la consulta de automoviles. ERROR :{e}",
        })
        raise HTTPException(500, 'Error Interno')
    else:
        logger.info({
            'timestamp': datetime.now(), 'level': "INFO",
            'message': "Se ha completado la peticion para consultar los vehiculos.",
        })
        return result


@router.put("/", response_model=str)
def create_car(license: str, color: str, brand: str):
    logger.info({
        'timestamp': datetime.now(), 'level': "INFO",
        'message': f"Se ha iniciado la peticion para crear el automovil {license}.",
    })
    try:
        car = car_register.search_car(license)
        if car:
            logger.warning({
                'timestamp': datetime.now(), 'level': "WARNING",
                'message': f"Se ha intentado crear el ya existente automovil {license}",
            })
            return 'El vehiculo ya existe'

        new_car = Car(license=license, color=color, brand=brand)
        car_register.add_car(new_car)
        save_to_database()

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(), 'level': "ERROR",
            'message': f"No se completo la creacion de automovil {license}. ERROR :{e}",
        })
    else:
        logger.info({
            'timestamp': datetime.now(), 'level': "INFO",
            'message': "Se completo la creacion de automovil {license}.",
        })
        return f"Se ha añadido al registro el coche {str(new_car)}"


@router.delete("/", response_model=str)
def remove_car(license: str):
    logger.info({
        'timestamp': datetime.now(), 'level': "INFO",
        'message': f"Se ha iniciado la peticion para eliminar el automovil {license}.",
    })
    try:
        car = car_register.search_car(license)
        if not car:
            logger.warning({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': f"Se ha intentado eliminar del registro el inexistente automovil {license}",
            })
            return 'El vehiculo no existe'

        car_register.delete_car(license)
        save_to_database()

    except Exception as e:
        logger.error({
                'timestamp': datetime.now(), 'level': "ERROR",
                'message': f"No se completo la eliminacion del automovil {license}. ERROR :{e}",
            })
    else:
        logger.info({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': f"Se Elimino del registro el automovil {license}",
            })
        return f"Se ha eliminado al registro el coche {str(car)}"
