from classLibrary.User import User
from peewee import *


def RegistrationUser():
    name = input("Ведите имя")
    surname = input("Ведите фамилию")
    phone = input("Ведите номер телефона")
    email = input("Ведите адрес электронной почты")
    user = User(name=name,surname=surname,phone=phone,email=email)
    user.save()

def ChangeUserByPhone(phone:str):
    user = User.select().where(User.phone == phone).get()
    return user
