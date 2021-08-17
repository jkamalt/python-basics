# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
from helper import try_parse


def get_salary(work_hours, hour_rate, bonus):
    """
    Вычисляет заработную плату с учетом работы в часах, ставки в час и премии.
    :param work_hours: работа в часах
    :param hour_rate: ставка в час
    :param bonus: премия
    :return: заработная плата
    """
    return work_hours * hour_rate + bonus


def main():
    try:
        work_hours = argv[1]
        hour_rate = argv[2]
        bonus = argv[3]
    except IndexError:
        print('Необходимо три параметра: 1 - работа в часах, 2 - ставка в час, 3 - премия')
    else:
        errors = []

        work_hours = try_parse(work_hours, float)
        if work_hours is None or work_hours < 0:
            errors.append('Некорректные данные для параметра "работа в часах"')

        hour_rate = try_parse(hour_rate, float)
        if hour_rate is None or hour_rate < 0:
            errors.append('Некорректные данные для параметра "ставка в час"')

        bonus = try_parse(bonus, float)
        if bonus is None or bonus < 0:
            errors.append('Некорректные данные для параметра "премия"')

        for error in errors:
            print(error)

        if errors:
            return

        print(f'Заработна плата равна: {get_salary(work_hours, hour_rate, bonus)}')


main()
