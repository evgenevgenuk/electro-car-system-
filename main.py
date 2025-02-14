class Car:
    def __init__(self, fuel: float = 0):
        self.__fuel = fuel

    def refuel(self, amount: float):
        if amount > 0:
            self.__fuel += amount

    @property
    def fuel(self):
        return self.__fuel


class ElectricCar(Car):
    def __init__(self, battery_charge: float = 0):
        super().__init__(0)
        self.__battery_charge = max(0, min(100, battery_charge))

    def refuel(self, amount: float):
        if amount > 0:
            self.__battery_charge = min(100, self.__battery_charge + amount)

    @property
    def battery_charge(self):
        return self.__battery_charge


car = Car(10)
electric_car = ElectricCar(50)

car.refuel(20)
electric_car.refuel(30)

print(car.fuel)  # 30
print(electric_car.battery_charge)  # 80
