from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_booking_list():
    response = client.get("/bookings/")
    assert response.status_code == 200
    assert response.json() == [
        "El dia 08-03-2025 estan alquilados los coches 8883EDW, 3869YTH, 1136PLO",
        "El dia 09-03-2025 estan alquilados los coches 8883EDW, 3869YTH, 9334BHW",
        "El dia 10-03-2025 estan alquilados los coches 8883EDW, 3869YTH, 2971UIT, 1136PLO, 9334BHW",
        "El dia 11-03-2025 estan alquilados los coches 2971UIT",
        "El dia 12-03-2025 estan alquilados los coches 3869YTH, 2971UIT",
        "El dia 13-03-2025 estan alquilados los coches 9334BHW"
    ]


def test_new_booking():
    response = client.post("/bookings/", json={'day': '09-03-2025', 'license': '3869YTH'})
    assert response.status_code == 200
    assert response.json() == "El vehiculo no esta disponible para ese dia. Intente otro dia"

    response = client.post("/bookings/", json={'day': '10-03-2025', 'license': ''})
    assert response.status_code == 200
    assert response.json() == "Actualmente no disponemos de ningun coche disponible para ese dia. Intente otro dia"

    response = client.post("/bookings/", json={'day': '09-03-2025', 'license': ''})
    assert response.status_code == 200
    assert response.json() == "Se ha guardado la reserva para el dia 09-03-2025 para el vehiculo Opel Corsa (2971UIT) de color Azul"

    response = client.post("/bookings/", json={'day': '13-03-2025', 'license': '3869YTH'})
    assert response.status_code == 200
    assert response.json() == "Se ha guardado la reserva para el dia 13-03-2025 para el vehiculo Seat Leon (3869YTH) de color Rojo"
