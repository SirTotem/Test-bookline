from app.models.booking import BookingRegister
from app.models.car import CarRegister
from app.db.database_helper import DatabaseHelper

car_register = CarRegister()
booking_register = BookingRegister()


def save_to_database():
    data = {'cars': car_register.to_dict(),
            'bookings': booking_register.to_dict()}
    DatabaseHelper.write_database(data)
