# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
from helper import try_parse


def division(numerator: float, denominator: float) -> float:
    """
    Вычисляет результат деления двух чисел
    :param numerator: Делимое
    :param denominator: Делитель
    :return: Результат деления
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print('Ошибка деления на 0')


def main():
    numerator = try_parse(input('Введите делимое: '), float)
    if numerator is None:
        print('Некорректные данные')
        return

    denominator = try_parse(input('Введите делитель: '), float)
    if denominator is None:
        print('Некорректные данные')
        return

    result = division(numerator, denominator)
    if result:
        print(f'Результат деление {numerator}/{denominator} = {result}')


main()
