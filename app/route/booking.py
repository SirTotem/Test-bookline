from typing import List
from fastapi import APIRouter

from app.log.logger import logger
from datetime import datetime

from app.route.register import booking_register
router = APIRouter()



@router.get("/", response_model=List[str])
def get_bookings():
    try:
        return booking_register.get_bookings()
    finally:
        logger.info({
            'timestamp': datetime.now(),
            'level': "INFO",
            'message': "Se completo una consulta a todas las reservas",
        })