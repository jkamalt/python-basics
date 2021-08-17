# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
from helper import try_parse


def get_pow_loop(base: float, exp: int) -> float:
    """
    Выполняет возведение числа base в степень exp с помощью цикла
    :param base: основание - действительное и положительное число
    :param exp: показатель - целое число
    :return: результат возведения числа base в степень exp
    """
    result = 1
    for i in range(abs(exp)):
        result *= base

    result = result if exp >= 0 else 1 / result
    return result


def get_pow_operator(base: float, exp: int) -> float:
    """
    Выполняет возведение числа base в степень exp с помощью оператора
    :param base: основание - действительное и положительное число
    :param exp: показатель - целое число
    :return: результат возведения числа base в степень exp
    """
    return base ** exp


def main():
    base = try_parse(input('Введите основание - действительное положительное число: '), float)
    if base is None or base <= 0:
        print('Некорректные данные')
        return

    exp = try_parse(input('Введите показатель - целое число: '), int)
    if exp is None:
        print('Некорректные данные')
        return

    print(f'Результат возведение числа {base} в степень {exp}:')
    print(f'1 способ: {get_pow_loop(base, exp)}')
    print(f'2 способ: {get_pow_operator(base, exp)}')


main()
