# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


def get_multiples(a, b, *divisors):
    """
    Возвращает список чисел в диапазоне [a, b], включая границы, кратных хотя бы одному числу из списка divisors
    :param a: начало диапазона
    :param b: конец диапазона
    :param divisors: список делителей
    :return: список чисел, кратных хотя бы одному числу из списка divisors
    """
    multiples = [number for number in range(a, b + 1) if is_multiple(number, *divisors)]
    return multiples


def is_multiple(number, *divisors):
    """
    Прверяет кратно ли число number хотя бы одному числу из списка divisors, в этом случае возвращает True, иначе False.
    :param number: преверяемое число
    :param divisors: список делителей
    :return: True, если кратно хотя бы одному числу из divisors, иначе False
    """
    result = False
    for divisor in divisors:
        result = result or number % divisor == 0
    return result


def main():
    a = 20
    b = 240
    divisors = [20, 21]
    multiples = get_multiples(a, b, *divisors)

    print('Список делителей:')
    print(divisors)

    print(f'Список чисел в диапазоне [{a}, {b}], включая границы, кратные хотя бы одному числу из списка делителей:')
    print(multiples)


main()
