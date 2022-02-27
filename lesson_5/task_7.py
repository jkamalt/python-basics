# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
from helper import read_rows, try_parse
from numpy import mean
from json import dump
from re import split

ownership_forms = ['ИП', 'ООО', 'ОАО', 'ЗАО', 'ПАО']


def get_firms_data(rows: list) -> dict:
    """
    Возвращает словарь {'Название фирмы': прибыль, ... } с данными по всем компаниям.
    :param rows: список строк с данными компании 'название_фирмы форма_собственности выручка издержки'
    :return: словарь {'Название фирмы': прибыль, ... } с данными по всем компаниям
    """
    firms_data = {}
    for row in rows:
        data = split('|'.join(ownership_forms), row)

        if len(data) >= 2:
            name = data[0].strip()
            numerical_data = data[1].split()

            if len(numerical_data) >= 2:
                numerical_data = [try_parse(number, float) for number in numerical_data]
                if None not in numerical_data:
                    profit = numerical_data[0] - numerical_data[1]
                    firms_data[name] = profit
    return firms_data


def get_average_profit(firms_data: dict):
    """
    Вычисляет среднюю прибыль по всем компаниям без учета компаний с отрицательной прибылью
    :param firms_data: словарь {'Название фирмы': прибыль, ... } с данными по всем компаниям
    :return: средняя прибыль по всем компаниям без учета компаний с отрицательной прибылью
    """
    profits = [val for val in firms_data.values() if val > 0]
    return mean(profits)


def write_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        dump(data, f)


def main():
    file_name = 'task_7.txt'
    json_file_name = 'task_7.json'

    rows = read_rows(file_name)
    firms_data = get_firms_data(rows)
    average_profit = get_average_profit(firms_data)

    print('Список: название фирмы и ее прибыль:')
    print(firms_data)
    print(f'Средняя прибыль по всем компаниям без учета отрицательной прибыли: {average_profit}')

    result = [firms_data, {'average_profit': average_profit}]
    write_json(json_file_name, result)


main()
