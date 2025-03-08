from typing import List, Dict
from pydantic import BaseModel
from app.db.database_helper import DatabaseHelper


class BookingRegister(BaseModel):
    booking_database: Dict[str, List[str]]

    def __init__(self):
        self.load_booking_database()
    
    def load_booking_database(self):
        db_helper = DatabaseHelper.read_database()
        for day, booking in db_helper.get("bookings", {}).items():
            self.booking_database[day]
            