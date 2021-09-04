from math import sqrt, isclose
from operator import add, sub, mul, truediv


class Complex:
    """
    Класс "комплексное число"
    """

    def __init__(self, real, imaginary):
        """
        Конструктор класса
        :param real: вещественная часть
        :param imaginary: мнимая часть
        """
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.is_real():
            return str(self.real)
        elif self.is_imaginary():
            return f'{self.imaginary}i'
        else:
            imag_abs = abs(self.imaginary)
            imag_str = 'i' if isclose(imag_abs, 1) else f'{imag_abs}i'
            return f'({self.real} + {imag_str})' if self.imaginary > 0 else f'({self.real} - {imag_str})'

    def __abs__(self):
        return sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return Complex(real, imaginary)

    def __truediv__(self, other):
        try:
            denominator = abs(other) ** 2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return Complex(real, imaginary)
        except ZeroDivisionError:
            print('Ошибка деления на комплексное число с модулем 0!')

    def is_real(self):
        """
        Определяет, является ли число вещественным (мнимая часть равна 0)
        :return: True, если число вещественное, иначе False
        """
        return isclose(self.imaginary, 0)

    def is_imaginary(self):
        """
        Определяет, явлется ли число чисто мнимым (вещественная часть равна 0)
        :return: True, если число чисто мнимое, иначе False
        """
        return isclose(self.real, 0)


def main():
    my_complex = []
    py_complex = []

    numbers = [(1, 2), (2, -3), (0, 2), (1, 0), (0, 0)]
    for number in numbers:
        my_complex.append(Complex(*number))
        py_complex.append(complex(*number))

    for my_number, py_number in zip(my_complex, py_complex):
        print(f'{my_number} = {py_number}')

    print('\n')

    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    my_1, my_2 = my_complex[:2]
    py_1, py_2 = py_complex[:2]
    for symbol, operator in operators.items():
        print(f'My: {my_1} {symbol} {my_2} = {operator(my_1, my_2)}')
        print(f'Py: {py_1} {symbol} {py_2} = {operator(py_1, py_2)}')
        print('\n')


main()
