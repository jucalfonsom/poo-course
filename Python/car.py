from account import Account


class Car:
    id = int
    license = str
    driver = Account(str, str)
    _passenger = int

    # Constructor
    def __init__(self, license: str, driver: str) -> None:
        self.license = license
        self.driver = driver

    # Using @property decorator
    @property
    
    # Getter method
    def passenger(self):
        if self._passenger != int:
            print(f'Passengers: {self._passenger}')
        else:
            print('Error with passenger')

    # Setter method
    @passenger.setter
    def passenger(self, passenger: int):
        if passenger == 4:
            self._passenger = int(passenger)
            print(f'Passengers assigned: {self._passenger}')
        else:
            print('You need to assign four passengers')