# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from helper import read_rows, write_rows

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def translate_rows(rows: list) -> list:
    """
    Возвращает новый список строк на основе списка rows, где первое слово в каждой строке заменено на русское слово.
    :param rows: исходный список строк
    :return: новый список строк, где первое слово в каждой строке заменено на русское слово
    """
    translated_rows = []
    for row in rows:
        words = row.split()
        if words:
            translated_rows.append(row.replace(words[0], translate[words[0]]))

    return translated_rows


def main():
    file_name = 'task_4.txt'
    new_file_name = 'task_4_new.txt'

    rows = read_rows(file_name)
    translated_rows = translate_rows(rows)
    write_rows(new_file_name, translated_rows)


main()
