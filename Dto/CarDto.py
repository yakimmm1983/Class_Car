from classLibrary.Car import Car
from peewee import *

def GetAllCar() -> list:
    cars = Car.select().dicts()
    inCars = []
    for car in cars:
        inCars.append(Car(id = Car["id"],nameCar = Car["nameCar"],namber = Car["number"]))
    return inCars


def GetCarById(Id:int)->Car:
    car = Car.select().where(Car.id == Id).get()
    return car