from account import Account


class Car:
    id = int
    license = str
    driver = Account("", "")
    __passenger = int

    # Constructor
    def __init__(self, license, driver) -> None:
        self.license = license
        self.driver = driver

    # Using @property decorator
    @property
    
    # Getter method
    def passenger(self):
        if self.__passenger != int:
            print(f'Passengers: {self.__passenger}')
        else:
            print('Error with passenger')

    # Setter method
    @passenger.setter
    def passenger(self, passenger: int):
        if passenger == 4:
            self.__passenger = int(passenger)
            print(f'Passangers assigned: {self.__passenger}')
        else:
            print('You need to assign four passengers')
