from typing import List, Dict
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

    def check_availability(self, day: str, license: str) -> bool:
        booking_day = self.booking_database.get(day, None)
        return (not booking_day or (not booking_day.contains(license)))
                
    def add_booking(self, day: str, license: str) -> None:
        if not self.booking_database.get(day, None):
            self.booking_database[day] = [license]
        else:
            self.booking_database[day].append(license)
    
    def get_all_bookings(self) -> List[str]:
        result = []
        for day, _ in self.booking_database.items():
            result.append(self.get_day_booking(day))

        return result
    
    def get_day_booking(self, day: str) -> str:
        return f"El dia {day} estan alquilados los coches {', '.join(self.booking_database.get(day, []))}"
