# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
from itertools import count, cycle


def print_count(start, stop):
    """
    Генерирует и выводит на экран целые числа, начиная с start до числа stop включительно.
    :param start: начало диапазона
    :param stop: конец диапазона
    """
    for number in count(start):
        if number > stop:
            break
        print(number)


def print_cycle(input_list, iterate_count):
    """
    Поочередно перебирает и выводит на экран элементы последовательности input_list iterate_count раз.
    :param input_list: входной список
    :param iterate_count: количество повторений
    """
    i = 1
    for item in cycle(input_list):
        if i > iterate_count:
            break
        print(item)
        i += 1


def main():
    start = 3
    stop = 10
    print(f'Итератор, генерирующий целые числа, начиная с {start} до {stop} включительно:')
    print_count(start, stop)

    input_list = list(range(10))
    iterate_count = len(input_list) * 2
    print(f'Итератор, повторяющий элементы списка {iterate_count} раз:')
    print_cycle(input_list, iterate_count)


main()
