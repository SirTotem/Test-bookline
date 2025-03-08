
from fastapi import FastAPI
from app.route import car
from app.route import booking


app = FastAPI()
app.include_router(car.router, prefix="/car", tags=["car"])
app.include_router(booking.router, prefix="/booking", tags=["booking"])
