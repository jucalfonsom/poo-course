# from car import Car
# from account import Account
# from user import User
from UberX import UberX


def run():
    # car = Car("AMS234", Account("Andres Herrera", "AND876"))
    # print(vars(car))
    # print(vars(car.driver))

    # user = User("Juan", "134234", "CC", "juan@test.com", "1234")
    # print(vars(user))

    print('UberX example')
    uberX = UberX("QWE345", "Juan Perez", "Renault", "Logan")
    print(vars(uberX))
    # Setting passenger
    uberX.passenger = 4
    # Use getter
    uberX.passenger


if __name__ == "__main__":
    run()