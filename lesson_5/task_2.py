# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from helper import read_rows


def get_words_count_in_row(rows: list) -> list:
    """
    Вычисляет количество слов, разделенных пробелами, в каждой строке списка rows и возвращает результат в виде списка.
    :param rows: список строк
    :return: список, содержащий количество слов в каждой строке входного списка
    """
    words_count = [len(row.split()) for row in rows]
    return words_count


def main():
    file_name = 'task_2.txt'

    rows = read_rows(file_name)
    words_count = get_words_count_in_row(rows)

    print(f'Количество строк в файле {file_name}: {len(rows)}')
    print('Количество слов в каждой строке:')
    for i, count in enumerate(words_count):
        print(f'Строка {i + 1}: {count}')


main()
