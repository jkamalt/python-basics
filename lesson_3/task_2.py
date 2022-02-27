# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def get_person_info(info_fields: tuple) -> dict:
    """
    Получает данные пользователя
    :param info_fields: ('Имя', 'Фамилия', ...) список полей данных пользователя
    :return: {'Имя': 'имя', ...} словарь поле - значения поля
    """
    person_info = {}
    for field in info_fields:
        person_info[field] = input(f'Введите значение поля "{field}": ')
    return person_info


def print_person_info_kwargs(**kwargs):
    """
    Выводит на экран строку с данными пользователя
    :param kwargs: данные пользователя
    """
    result = ''
    for field in kwargs:
        result += f'{field}: {kwargs[field]}; '
    print(result)


def print_person_info(name='', surname='', birth_year='', city='', email='', phone_number=''):
    """
    Выводит на экран строку с данными пользователя
    :param name: имя
    :param surname: фамилия
    :param birth_year: год рождения
    :param city: город проживания
    :param email: email
    :param phone_number: телефон
    """
    print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {birth_year}; '
          f'Город проживания: {city}; Email: {email}; Телефон: {phone_number};')


def main():
    info_fields = ('Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Email', 'Телефон')

    person_info = get_person_info(info_fields)

    print_person_info_kwargs(**person_info)
    print_person_info(name=person_info['Имя'], surname=person_info['Фамилия'], birth_year=person_info['Год рождения'],
                      city=person_info['Город проживания'], email=person_info['Email'],
                      phone_number=person_info['Телефон'])


main()
