# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


def create_list():
    """
    Создает список из произвольного числа элементов.
    Число элементов и сами элементы вводит пользователь
    """
    try:
        list_count = int(input('Введите число элементов в списке: '))
    except ValueError:
        print('Ошибка. Нужно ввести целое число!')
    except Exception:
        print('Неизвестная ошибка')
    else:
        input_list = []
        for i in range(list_count):
            item = input(f'Введите {i + 1} элемент списка: ')
            input_list.append(item)

        return input_list


def swap_elements(input_list):
    """
    Модифицирует список input_list.
    Значениями обмениваются элементы с индексами 0 и 1, 2 и 3, и т.д.
    При нечетном количестве элементов последний остается на месте
    """
    print(list(range(0, len(input_list) - 1, 2)))
    for i in range(0, len(input_list) - 1, 2):
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]


def main():
    input_list = create_list()
    print('Исходный список:')
    print(input_list)

    swap_elements(input_list)
    print('Список после обмена соседних элементов:')
    print(input_list)


main()
