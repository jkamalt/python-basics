# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def get_even_numbers(a, b):
    """
    Возвращает список четных чисел в диапазоне [a, b], включая границы.
    :param a: начало диапазона
    :param b: конец диапазона
    :return: список четных чисел
    """
    even_numbers = [number for number in range(a, b + 1) if number % 2 == 0]
    return even_numbers


def get_product(numbers):
    """
    Вычисляет произведение чисел списка.
    :param numbers: список чисел
    :return: произведение чисел
    """
    product = reduce(lambda x, y: x * y, numbers)
    return product


def main():
    a = 100
    b = 1000
    even_numbers = get_even_numbers(a, b)
    product = get_product(even_numbers)

    print(f'Список четных чисел в диапазоне [{a}, {b}], включая границы:')
    print(even_numbers)
    print(f'Результат вычисления произведения всех элементов:\n{product}')


main()
