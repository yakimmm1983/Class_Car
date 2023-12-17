from classLibrary.BaseModel import BaseModel
from classLibrary.Car import Car
from classLibrary.User import User
import datetime
from peewee import *


class RentInCar(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    dateStart = DateField(column_name="date_rent_start")
    dateEnd = DateField(column_name="date_rent_end")
    carRentTime = IntegerField(column_name = "car_rent_time")
    userRent = ForeignKeyField(User,related_name="rent_to_user",to_field="id")
    carRent = ForeignKeyField(Car, related_name="rent_to_car", to_field="id")




    class Meta:
        table_name = "RentInCar"