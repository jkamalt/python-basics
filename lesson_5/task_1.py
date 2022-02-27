# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
from helper import write_rows


def input_rows() -> list:
    """
    Запрашивает данные у пользователя и записывает полученные строки в список.
    :return: список строк, введенных пользователем
    """
    rows = []
    while True:
        input_str = input('Введите строку, для выхода введите пустую строку: ')
        if input_str is '':
            break
        rows.append(input_str)
    return rows


def main():
    file_name = 'task_1.txt'

    rows = input_rows()
    write_rows(file_name, rows)
    print(f'Введенные строки записаны в файл {file_name}')


main()
