# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


def print_elements_types(input_list):
    """Проверяет и выводит тип элементов входного списка с использованием цикла"""
    for item in input_list:
        print(f'{item}: {type(item)}')


def get_elements_types(input_list):
    """Возвращает список типов элементов входного списка. Используется генератор списков"""
    return [type(item) for item in input_list]


def get_elements_types_map(input_list):
    """Возвращает список типов элементов входного списка. Используется метод map"""
    return list(map(type, input_list))


def main():
    input_list = [1, 1.1, 'abc', True, [1, 2, 3], {'a': 1, 'b': 2}, (1, 2, 3), lambda x: x * 2]

    print(get_elements_types(input_list))
    print(get_elements_types_map(input_list))
    print_elements_types(input_list)


main()
