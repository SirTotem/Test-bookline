from typing import List, Dict
from pydantic import BaseModel
from app.db.database_helper import DatabaseHelper


class BookingRegister:
    booking_database: Dict[str, List[str]]

    def __init__(self):
        self.booking_database = {}
        self.load_booking_database()
    
    def load_booking_database(self) -> None:
        db_helper = DatabaseHelper.read_database()
        for day, booking in db_helper.get("bookings", {}).items():
            self.booking_database[day] = booking
    
    def get_all_bookings(self) -> str:
        result= ''
        for day, _ in self.booking_database:
            result += self.get_day_bookings(day)+'\n'

    def get_day_booking(day:str) -> str:
        return f"El dia {day} estan alquilados los coches {', '.join(self.booking_database.get(day, []))}"
