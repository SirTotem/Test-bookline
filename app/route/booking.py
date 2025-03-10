from typing import List
from fastapi import APIRouter

from app.log.logger import logger
from datetime import datetime

from app.db.register import booking_register, car_register, save_to_database
from app.models.booking import Booking

router = APIRouter()


@router.get("/", response_model=List[str])
def get_bookings():
    try:
        logger.info({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': "Se inicio una consulta a todas las reservas",
            })

        result = booking_register.get_all_bookings()

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(), 'level': "ERROR",
            'message': f"No se completo la consulta de reservas. ERROR :{e}",
        })
    else:
        logger.info({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': "Se completo una consulta a todas las reservas",
            })
        return result


@router.get("/{day}", response_model=str)
def get_bookings_by_day(day: str):
    try:
        logger.info({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': "Se inicio una consulta para las reservas del dia {day}",
            })
        result = booking_register.get_day_booking(day)
    except Exception as e:
        logger.error({
                'timestamp': datetime.now(), 'level': "ERROR",
                'message': f"No se completo la consulta de reservas del dia {day}. ERROR :{e}",
            })
    else:
        logger.info({
                'timestamp': datetime.now(), 'level': "INFO",
                'message': f"Se completo una consulta para las reservas del dia {day}",
            })
        return result


@router.post("/", response_model=str)
def add_booking(new_book: Booking):
    logger.info({
            'timestamp': datetime.now(), 'level': "INFO",
            'message': f"Se inicio una peticion para una reserva el dia {new_book.day} y el vehiculo {new_book.license}",
    })
    try:
        license = new_book.license
        day = new_book.day
        if license:
            if car_register.search_car(license):
                if booking_register.check_availability(day, license):
                    booking_register.add_booking(day, license)
                    response_model = f'Se ha guardado la reserva para el dia {day} para el vehiculo {str(car_register.search_car(license))}'

                    logger.info({
                        'timestamp': datetime.now(), 'level': "INFO",
                        'message': f"Se completo una nueva reserva para el dia {day} y el vehiculo {license}."
                    })
                else:
                    response_model = "El vehiculo no esta disponible para ese dia. Intente otro dia"
                    logger.warning({
                        'timestamp': datetime.now(), 'level': "WARNING",
                        'message': f"Se ha intentado hacer una reserva para un dia ({day}) y vehiculo ({license}) no disponibles  ",
                    })

            else:
                response_model = "Este vehiculo no esta presente en nuestro registro. No se ha hecho la reserva"
                logger.warning({
                        'timestamp': datetime.now(), 'level': "WARNING",
                        'message': f"Se ha intentado hacer una reserva para un vehiculo ({license}) no existente",
                    })

        else:
            response_model = "Actualmente no disponemos de ningun coche disponible para ese dia. Intente otro dia"
            for license, _ in car_register.car_database.items():
                if booking_register.check_availability(day, license):
                    booking_register.add_booking(day, license)
                    response_model = f'Se ha guardado la reserva para el dia {day} para el vehiculo {str(car_register.search_car(license))}'
                    break

            logger.warning({
                        'timestamp': datetime.now(), 'level': "WARNING",
                        'message': f"Se ha intentado hacer una reserva para un dia ({day}) sin vehiculos disponibles",
                    })
        save_to_database()
        logger.info({
                    'timestamp': datetime.now(), 'level': "WARNING",
                    'message': f"El registro actual de reservas para el dia {day} es: {booking_register.get_day_booking(day)}",
        })
        return response_model

    except Exception as e:
        logger.error({
            'timestamp': datetime.now(), 'level': "ERROR",
            'message': f"No se completo una nueva reserva para el dia {day} y el vehiculo {license}. ERROR :{e}",
        })
