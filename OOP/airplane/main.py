class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def take_off(self):
        print('Houston, we`re taking off ...')
        self.is_flying = True

    def fly(self, flown_range):
        print(f'mayday, we managed to fly {flown_range}')
        self.odometer += flown_range
        print(f'At the moment odometer reading is {self.odometer}')

    def land(self):
        print('Appolon 13, we have to land soon')
        print('Appolon 13: Roger that!')
        self.is_flying = False


airbus_a_330 = Airplane('Airbus', 'a330', 2010, 1100, 300000000)

airbus_a_330.take_off()
print(airbus_a_330.is_flying)
print('-' * 30)
airbus_a_330.land()
print(airbus_a_330.is_flying)
airbus_a_330.fly(500000)
