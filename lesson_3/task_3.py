# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов
from helper import try_parse


def get_two_max_sum(a: float, b: float, c: float) -> float:
    """
    Вычисляет сумму наибольших двух аргументов
    :param a: Первое число
    :param b: Второе число
    :param c: Третье число
    :return: Сумма наибольших двух аргументов
    """
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers, reverse=True)
    return sum(sorted_numbers[:2])


def main():
    a = try_parse(input('Введите первое число: '), float)
    if a is None:
        print('Некорректные данные')
        return

    b = try_parse(input('Введите второе число: '), float)
    if b is None:
        print('Некорректные данные')
        return

    c = try_parse(input('Введите третье число: '), float)
    if c is None:
        print('Некорректные данные')
        return

    result = get_two_max_sum(a, b, c)
    print(f'Сумма двух наибольших чисел из заданных [{a}, {b}, {c}]:\n{result}')


main()
