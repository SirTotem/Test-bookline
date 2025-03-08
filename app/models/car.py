from pydantic import BaseModel


class Car(BaseModel):
    brand: str
    license: str

    def __str__(self):
        return self.brand + " (" + self.license + ")"
