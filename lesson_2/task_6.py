# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


def print_menu():
    """Выводит меню"""
    print('1. Внести данные\n2. Вывести данные\n3. Вывести аналитику по товарам\n4. Выход')


def show_data(data):
    """Выводит данные на экран"""
    for entry in data:
        print(entry)


def create_new_entry(fields):
    """
    Создает новую запись
    :param fields: ('название', 'цена', ...) - список полей записи
    :return: {'название': 'компьютре', 'цена': 20000, ...} - новая запись
    """
    entry = {}
    for field in fields:
        value = input(f'Введите значение поля "{field}": ')
        entry[field] = int(value) if value.isdigit() else value
    return entry


def show_data_analytics(fields, data):
    """
    Выводит аналитику по товарам на экран
    :param fields: ('название', 'цена', ...) - список полей записи
    :param data: список записей
    """
    analytics = {}
    for field in fields:
        analytics[field] = [entry[1][field] for entry in data]
    print(analytics)


def main():
    data = []
    entry_fields = ('название', 'цена', 'количество', 'ед')

    while True:
        print_menu()
        choice = input('Введите пункт меню: ')

        if choice == '1':
            data.append((len(data) + 1, create_new_entry(entry_fields)))
        elif choice == '2':
            show_data(data)
        elif choice == '3':
            show_data_analytics(entry_fields, data)
        elif choice == '4':
            break
        else:
            print('Выберите правильный пункт меню')

        print('\n')


main()
