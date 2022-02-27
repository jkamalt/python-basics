# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(number):
    """
    Вычисляет факториал числа number
    :param number: число, для которого вычисляется факториал
    :return: генератор
    """
    if number == 0:
        yield 1

    result = 1
    for n in range(1, number + 1):
        result *= n
        yield result


def main():
    n = 5
    for el in fact(n):
        print(el)


main()