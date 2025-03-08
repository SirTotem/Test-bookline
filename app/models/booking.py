from pydantic import BaseModel
import datetime

from app.models.car import Car


class Booking(BaseModel):
    registred_car: Car
    date: datetime.date

