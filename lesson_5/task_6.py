# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
from helper import read_rows, get_row_sum

str_to_delete = ['(л)', '(пр)', '(лаб)']


def get_lessons_data(rows: list) -> dict:
    """
    Возвращает словарь {'название предмента': количество занятий, ... } с данными по всем предметам.
    :param rows: список строк с данными по предмету 'название предмета: n1(л) n2(пр) n3(лаб)'
    :return: словарь {'название предмента': количество занятий, ... } с данными по всем предметам
    """
    lessons_data = {}
    for row in rows:
        data = row.split(':')

        if len(data) >= 2:
            name = data[0]
            count = get_row_sum(clear_str(data[1]), int)
            lessons_data[name] = count

    return lessons_data


def clear_str(input_str: str) -> str:
    """
    Удаляет из входной строки все подстроки, равные элементам списка str_to_delete
    :param input_str: входная строка
    :return: строка на основе входной строки, у которой удалены подстроки, равные элементам списка str_to_delete
    """
    for el in str_to_delete:
        input_str = input_str.replace(el, '')
    return input_str


def main():
    file_name = 'task_6.txt'

    rows = read_rows(file_name)
    lessons_data = get_lessons_data(rows)

    print('Количество занятий для каждого предмета:')
    print(lessons_data)


main()
