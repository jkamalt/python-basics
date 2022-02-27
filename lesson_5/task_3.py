# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from helper import read_rows, try_parse
from numpy import mean


def get_employees_data(rows: list) -> dict:
    """
    Возвращает словарь {'фамилия1': зарплата1, 'фамилия2': зарплата2, ... } с данными сотрудников.
    :param rows: список строк с данными сотрудника 'фамилия зарплата'
    :return: словарь {'фамилия1': зарплата1, 'фамилия2': зарплата2, ... } с данными сотрудников
    """
    employees_data = {}
    for row in rows:
        employee_data = row.split()

        if len(employee_data) >= 2:
            salary = try_parse(employee_data[1], float)
            if salary is not None:
                employees_data[employee_data[0]] = salary

    return employees_data


def get_average_salary(employees_data: dict):
    """
    Вычисляет среднюю величину дохода сотрудников.
    :param employees_data: словарь {'фамилия1': зарплата1, 'фамилия2': зарплата2, ... } с данными сотрудников
    :return: средняя величина дохода сотрудников
    """
    salaries = [val for val in employees_data.values()]
    return mean(salaries)


def get_employees_under_min_salary(employees_data: dict, min_salary: float) -> list:
    """
    Возвращает список с фамилиями сотрудников, которые имеют оклад менее min_salary.
    :param employees_data: словарь {'фамилия1': зарплата1, 'фамилия2': зарплата2, ... } с данными сотрудников
    :param min_salary: минимальный доход
    :return: список с фамилиями
    """
    employees = [key for key, val in employees_data.items() if val < min_salary]
    return employees


def main():
    file_name = 'task_3.txt'
    min_salary = 20000

    rows = read_rows(file_name)
    employees_data = get_employees_data(rows)
    average_salary = get_average_salary(employees_data)
    employees_under_min_salary = get_employees_under_min_salary(employees_data, min_salary)

    print(f'Средняя величина дохода сотрудников: {average_salary}')
    print(f'Сотрудники, которые имеют оклад менее {min_salary}:')
    print(employees_under_min_salary)


main()
