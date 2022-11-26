class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def __str__(self):
        return f'Phone number : {self.number}\n' \
               f'Phone model: {self.model}\n' \
               f'Phone weight {self.weight}'

    def sendMessage(self, *args):
        print('Phone numbers to which messages will be sent')
        for i in args:
            print(i)


pocophone = Phone(996700757113, 'f3', 205)
samsung = Phone(996552502060, 'a51', 215)
iphone = Phone(996990833833, '13', 210)

print(pocophone)
pocophone.sendMessage(996700100100, 996707123123, 996555525252, 996703111993)
