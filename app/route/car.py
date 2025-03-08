from typing import List
from fastapi import APIRouter

from app.models.car import CarRegister

router = APIRouter()
car_register = CarRegister()


@router.get("/", response_model=List[str])
def get_cars():
    return car_register.get_cars()
