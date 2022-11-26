class Person:
    def __init__(self, full_name, address, age=18):
        self.full_name = full_name
        self.age = age
        self.address = address

    def talk(self):
        print(f'{self.full_name} говорит')

    def move(self, new_address):
        self.address = new_address

    def __str__(self):
        return f'full name: {self.full_name}\n' \
               f'Address is : {self.address} \n' \
               f'Age is: {self.age}'


vasya = Person('Vasya Pupkin', 'Moscow', 20)
print(vasya)
vasya.move('Petersburg')
print(vasya)
vasya.talk()





