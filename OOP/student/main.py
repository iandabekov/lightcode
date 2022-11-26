class Student:
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f'{self.name} {self.last_name} поступил в {self.year_of_entrance} г. на факультет: {self.department}.')


s = Student('Vasya', 'Pupkin', 'Восточные культуры', 2020)

s.get_student_info()
