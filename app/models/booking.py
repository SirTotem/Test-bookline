from pydantic import BaseModel
from models.car import Car
import datetime


class BookingRegister(BaseModel):
    registred_car: Car
    date: datetime.date
