from classLibrary.BaseModel import BaseModel
from peewee import *


class Car(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    nameCar = CharField(column_name="nameCar", max_length=120)
    number = CharField(column_name="number", max_length=20)


    class Meta:
        table_name = "car"
