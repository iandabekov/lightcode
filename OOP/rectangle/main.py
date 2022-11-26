
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.demonstration()

    def perimeter(self):
        print((self.a + self.b) * 2)

    def area(self):
        print(self.a * self.b)

    def sizes_change(self, a=None, b=None):
        if a is None and b is None:
            pass
        elif a and b is None:
            self.a = a
        elif b and a is None:
            self.b = b
        elif a and b:
            self.a = a
            self.b = b
        print(f'Сторона а: {self.a}\n'
              f'Сторона б: {self.b}')

    def demonstration(self):
        answer = ' '
        while answer != '' and answer != 'end':
            print(f'Здравствуйте, введите одно из этих команд ("периметр", "площадь", "изменить размер", если хотите выйти нажмите enter или "end")')
            answer = input()
            if answer == 'периметр':
                self.perimeter()
            elif answer == 'площадь':
                self.area()
            elif answer == 'изменить размер':
                side = input('Какую сторону хотите изменить(a, b, обе): ')
                if side == 'a':
                    a = int(input('Введите сторону a: '))
                    self.sizes_change(a=a)
                elif side == 'b':
                    b = int(input('Введите сторону b: '))
                    self.sizes_change(b=b)
                elif side == 'обе':
                    a = int(input('Введите сторону a: '))
                    b = int(input('Введите сторону b: '))
                    self.sizes_change(a, b)


rectangle1 = Rectangle(10, 15)


