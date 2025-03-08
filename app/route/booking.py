from typing import List
from fastapi import APIRouter

from app.log.logger import logger
from datetime import datetime

from app.db.register import booking_register
from app.db.register import car_register
router = APIRouter()


@router.get("/", response_model=List[str])
def get_bookings():
    try:
        return booking_register.get_all_bookings()
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se completo una consulta a todas las reservas",
        })


@router.get("/{day}", response_model=str)
def get_bookings_by_day(day: str):
    try:
        return booking_register.get_day_booking(day)
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se completo una consulta para las reservas del dia {day}",
        })


@router.put("/{day}", response_model=str)
def add_booking(day: str, license: str = None):
    try:
        if license:
            if car_register.search_car(license):
                if booking_register.check_availability(license, day):
                    response_model = f'Se ha guardado la reserva para el dia {day} para el vehiculo {str(car_register.search_car(license))}'
                else:
                    response_model = "El vehiculo disponible para ese dia. Intente otro dia"


            else:
                response_model = "Este vehiculo no esta presente en nuestro registro. No se ha hecho la reserva"
        
        else:
            for license, _  in car_register.car_database.items():
                if booking_register.check_availability(license, day):
                    booking_register.add_booking(license,day)
                    response_model = f'Se ha guardado la reserva para el dia {day} para el vehiculo {str(car_register.search_car(license))}'
                    break;
            response_model = "Actualmente no disponemos de ningun coche disponible para ese dia. Intente otro dia"


        return booking_register.get_day_booking(day)
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se completo una consulta para las reservas del dia {day}",
        })