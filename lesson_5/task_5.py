# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from helper import read_rows, get_row_sum


def main():
    file_name = 'task_5.txt'

    rows = read_rows(file_name)
    for i, row in enumerate(rows):
        print(f'Сумма чисел в {i + 1} строке: {get_row_sum(row, float)}')


main()
