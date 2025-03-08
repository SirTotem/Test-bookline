from pydantic import BaseModel
from typing import Dict

from app.db.database_helper import DatabaseHelper


class Car(BaseModel):
    license: str
    brand: str
    color: str

    def __str__(self):
        return self.brand + " (" + self.license + ")"


class CarRegister:
    car_database: Dict[str, Car]

    def __init__(self):
        self.car_database = {}
        self.read_car_database()

    def read_car_database(self):
        db_helper = DatabaseHelper.read_database()
        for license, car in db_helper.get("cars", {}).items():
            self.car_database[license] = Car(license=license,
                                             brand=car.get('brand'),
                                             color=car.get('color'))

    def get_cars(self):
        return [str(car) for _, car in self.car_database.items()]

    def search_car(self, license: str) -> Car:
        return self.car_database.get(license, None)


    def add_car(self, car: Car):
        if not self.search_car(Car.license):
            self.car_database.append(car)
            DatabaseHelper.write_cars(self.car_database)
        else:
            pass

    def delete_car(self, license: str):
        del self.car_database[license]
        DatabaseHelper.write_cars(self.car_database)