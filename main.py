from classLibrary import Car,RentInCar,User
from Dto import CarDto,RentInCarDto,UserDto


def regUser():
    name = input("Ведите имя")
    surname = input("Ведите фамилию")
    phone = input("Ведите номер телефона")
    email = input("Ведите адрес электронной почты")
    UserDto.RegistrationUser(phone,name,surname,email)

def SeeAllCar()->str:
    car = ""
    cars = CarDto.GetAllCar()
    for book in cars:
        car+=f"{car.id} {car.nameCar} {car.number}\n"
    return car

def rentToCar():
    userPhone = input("Найдите себя по номеру телефона или пройдите регистрацию")
    try:
        user = UserDto.ChangeUserByPhone(userPhone)
    except Exception:
        user = regUser()
    try:
        carId = int(input("Введите номер машины из списка"))
        car = CarDto.GetCarById(carId)

    except Exception:
        print("Не удалось найти автомобиль")
def CreateRent():
    if rentToCar() == True:
        createRent = input("Аренда автомобиля выдается посуточно!\n"
                       "На сколько суток вы хотите взять автомобиль?")
        createRent.save()
        RentInCarDto.startRent()


    _mainMenu = "1-регистрация, 2-посмотреть автомобили, 3-срок аренды, 4-взять автомобиль в аренду,5-выход"
    choise = input(_mainMenu)
    if choise =="1":
        regUser()
    elif choise =="2":
        SeeAllCar()
    elif choise =="3":
        CreateRent()
    elif choise =="4":
        rentToCar()
    elif choise =="5":
        break
    else:
       pass



