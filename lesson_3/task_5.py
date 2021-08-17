# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
from helper import try_parse


def get_sum(numbers):
    """
    Вычисляет сумму чисел, заданных как список строк
    :param numbers: Числа в виде списка строк
    :return: Сумма чисел, которых удалось преобразовать в число
    """
    result = 0
    for number in numbers:
        number = try_parse(number, float)
        if number is not None:
            result += number
    return result


def main():
    is_exit = False
    result = 0
    while not is_exit:
        print('Для выхода введите q')

        input_str = input('Введите числа, разделенные пробелами: ')
        numbers = input_str.split()

        if 'q' in numbers:
            is_exit = True
            numbers = numbers[:numbers.index('q')]

        result += get_sum(numbers)
        print(result)


main()
