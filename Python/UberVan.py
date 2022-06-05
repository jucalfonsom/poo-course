from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial

    # Override method setPassenger of super class Car for apply Polymorphism
    # Setter method
    @Car.passenger.setter
    def passenger(self, passenger: int):
        if passenger == 6:
            self._passenger = int(passenger)
            print(f'Passengers assigned: {self._passenger}')
        else:
            print('You need to assign four passengers')