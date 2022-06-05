from car import Car
from account import Account


def run():
    car = Car("AMS234", Account("Andres Herrera", "AND876"))
    print(vars(car))
    print(vars(car.driver))


if __name__ == "__main__":
    run()