from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_cars():
    response = client.get("/cars/")
    assert response.status_code == 200
    assert response.json() == [
        "Toyota Prius (8883EDW) de color Azul",
        "Seat Leon (3869YTH) de color Rojo",
        "Opel Corsa (2971UIT) de color Azul",
        "Honda Civic (1136PLO) de color Amarillo",
        "Seat Ibiza (9334BHW) de color Negro",
        ]

