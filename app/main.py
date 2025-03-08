
from fastapi import FastAPI
from app.route import booking, car


app = FastAPI()
app.include_router(car.router, prefix="/cars", tags=["cars"])
app.include_router(booking.router, prefix="/bookings", tags=["bookings"])
