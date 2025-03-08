from typing import List
from pydantic import BaseModel

from app.db.database_helper import DatabaseHelper


class Car(BaseModel):
    license: str
    brand: str

    def __str__(self):
        return self.brand + " (" + self.license + ")"


class CarRegister:
    car_database: List[Car]

    def __init__(self):
        self.update_car_database()
    
    def update_car_database(self):
        db_helper = DatabaseHelper.read_database()
        self.car_database = [Car(**car) for car in db_helper.get("cars", [])]

    def get_cars(self):
        return [str(car) for car in self.car_database]

    def search_car(self, license: str) -> Car:
        for car in self.car_database:
            if car.liscense == license:
                return car
        return None

    def get_details_by_license(self, license: str) -> dict:
        
        car = self.search_car()
        if car:
            return str(car)

        return None

    def add_car(self, car: Car):
        if not self.search_car(Car.license):
            self.car_database.append(car)
            DatabaseHelper.write_cars(self.car_database)
        else:
            pass

    def delete_car(self, car: Car):
        db = DatabaseHelper.read_database()
        pass