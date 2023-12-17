from peewee import *
db = PostgresqlDatabase('RentInCar', host='localhost',port = 5432,user='postgres',password='1')


class BaseModel(Model):
    class Meta:
        database = db