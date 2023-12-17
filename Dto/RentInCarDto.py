from classLibrary.BaseModel import BaseModel
from classLibrary.Car import Car
from classLibrary.User import User
from classLibrary.RentInCar import RentInCar
import datetime
from peewee import *

def GetAllRentInCar() -> list:
    cars = RentInCar.select().dicts()
    rentInCars = []
    for car in rentInCars:
        rentInCars.append(RentInCar(id = RentInCar["id"],carRentTime = RentInCar["carRentTime"],
                                    userRent = RentInCar["userRent"],carRent = RentInCar["carRent"]))
    return GetAllRentInCar()


def GetRentInCarById(Id:int):
    car = RentInCar.select().where(RentInCar.id == Id).get()
    return GetRentInCarById()

def startRent(data,name,surname,nameCar,number):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    rent = RentInCar(data = data, name = name, surname = surname, nameCar = nameCar, number = number)
    rent.save()
    return rent

def endRent():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    date.save()


