from car import Car
from account import Account
from user import User


def run():
    car = Car("AMS234", Account("Andres Herrera", "AND876"))
    print(vars(car))
    print(vars(car.driver))

    user = User("Juan", "134234", "CC", "juan@test.com", "1234")
    print(vars(user))


if __name__ == "__main__":
    run()