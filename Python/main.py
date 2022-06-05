from car  import Car
from account import Account
from user import User
from UberX import UberX
from UberVan import UberVan


def run():
    car = Car("AMS234", Account("Andres Herrera", "AND876"))
    print(vars(car))
    print(vars(car.driver))

    user = User("Juan", "134234", "CC", "juan@test.com", "1234")
    print(vars(user))

    print('-' * 40)
    print('UberX example')
    uberX = UberX(license='QWE345', driver=Account('Juan Perez', '12343134'), brand='Renault', model='Logan')
    print(vars(uberX))
    print(vars(uberX.driver))
    uberX.passenger = 4 # Setting passenger
    uberX.passenger # Use getter


    print('-' * 40)
    print('UberVan example')
    uberVan = UberVan(license='VAN123', driver=Account('Pedro Rodriguez', '98765432'), typeCarAccepted=['Mercedes Benz'], seatsMaterial=['Synthetic'])
    print(vars(uberVan))
    print(vars(uberVan.driver))
    # UberVan should have 6 passengers
    uberVan.passenger = 6
    uberVan.passenger


if __name__ == "__main__":
    run()