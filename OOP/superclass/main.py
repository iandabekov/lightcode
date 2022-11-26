class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Person name: {self.name}\n'
              f'Person age = {self.age}')


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f'Student name: {self.name}\n'
              f'Student age = {self.age}\n'
              f'Student section = {self.section}')


P = Person("Tomas Wild", 37)

P.display()
print('-' * 30)
S = Student("Albert", 23, "Mathematics")

S.displayStudent()
