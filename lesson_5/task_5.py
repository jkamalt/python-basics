# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from helper import read_rows, get_row_sum, write_rows
from random import randint


def main():
    file_name = 'task_5.txt'

    numbers = [str(randint(-10, 10)) for _ in range(10)]
    write_rows(file_name, [' '.join(numbers)])

    rows = read_rows(file_name)
    print('Набор чисел:', rows[0])
    print(f'Сумма чисел: {get_row_sum(rows[0], int)}')


main()
