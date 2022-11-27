class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, distance):
        if distance / 100 * 10 <= self.fuel:
            print(f'{self.odometer} odometer, {self.fuel} fuel')
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
            print('Let`s drive! ')
            print(f'{self.odometer} odometer, {self.fuel} fuel')

        else:
            print('Need more fuel, please, fill more!')

    def __add_distance(self, distance):
        if isinstance(distance, (int, float)):
            self.odometer += distance
            return self.odometer
        else:
            print("it's not a number")

    def __subtract_fuel(self, distance):
        if isinstance(distance, (int, float)):
            self.fuel -= distance / 100 * 10
            return self.fuel
        else:
            print("it's not a number")


a = Car('merc', '210', 1998)

a.drive(distance=350)
