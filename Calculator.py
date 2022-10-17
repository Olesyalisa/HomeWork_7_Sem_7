# класс Комплексное число
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im,
                        self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        d = other.re*other.re + other.im * other.im

        return Complex((self.re * other.re - self.im * other.im) / d,
                        (self.re * other.im + self.im * other.re) / d)

    def __str__(self, mode=0):
        if (mode == 0):
            return str(self.re)

        s = " "
        if (self.im >= 0):
            s = ' + '

        return str(self.re) + s + str(self.im) + 'i'

a = Complex()
b = Complex()
mode = 0

while (True):
    print('A: ' + a.__str__(mode))
    print('B: ' + b.__str__(mode))

    print('1. Режим: ', end='')
    if (mode == 0):
        print('Действительные')
    else: #mode == 1
        print('Комплексные')
    print('2. Дейсвительная A')
    if (mode == 1):
        print('3. Мнимая A')
    print('4. Дейсвительная B')
    if (mode == 1):
        print('5. Мнимая B')
    print('6. Сложить')
    print('7. Вычесть')
    print('8. Умножить')
    print('9. Поделить')
    print('0. Выход')

    n = int(input('Выберите: '))

    if (n == 0):
        break
    if (n == 1): #Режим
        mode = 1-mode
    if (n == 2): #Дейсвительная A
        a.re = float(input('Введите: '))
    if (n == 3): #Мнимая A
        a.im = float(input('Введите: '))
    if (n == 4): #Дейсвительная B
        b.re = float(input('Введите: '))
    if (n == 5): #Мнимая B
        b.im = float(input('Введите: '))
    if (n == 6): #Сложить
        r = a + b
        print('Результат: ' + r.__str__(mode))
    if (n == 7): #Вычесть
        r = a - b
        print('Результат: ' + r.__str__(mode))
    if (n == 8): #Умножить
        r = a * b
        print('Результат: ' + r.__str__(mode))
    if (n == 9): #Поделить
        r = a / b
        print('Результат: ' + r.__str__(mode))
