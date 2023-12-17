from classLibrary.Car import Car
from classLibrary.User import User
from classLibrary.RentInCar import RentInCar

if __name__ == "__main__":
    status = "ok"
    try:
        RentInCar.drop_table()
        Car.drop_table()
        User.drop_table()

    except Exception as e:
        status = f"Drop error {e}"
    try:
        User.create_table()
        Car.create_table()
        RentInCar.create_table()

    except Exception as e:
        status = f"Create error {e}"
    print(f"Migration {status}")