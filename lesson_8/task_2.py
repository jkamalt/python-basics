from helper import try_parse


class OwnZeroDivisionError(Exception):
    """
    Исключение деления на 0
    """
    pass


def division(numerator: float, denominator: float) -> float:
    """
    Вычисляет результат деления двух чисел
    :param numerator: Делимое
    :param denominator: Делитель
    :return: Результат деления
    """
    try:
        if denominator == 0:
            raise OwnZeroDivisionError('Ошибка деления на 0!')
    except OwnZeroDivisionError as e:
        print(e)
    else:
        return numerator / denominator


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
