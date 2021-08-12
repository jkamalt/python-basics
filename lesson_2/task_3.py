# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


def get_season_dict_list(month_number):
    """Возвращает время года, к которому относится месяц с номером month_number. Используется словарь со списком"""
    seasons = {
        'Зима': [12, 1, 2],
        'Весна': [3, 4, 5],
        'Лето': [6, 7, 8],
        'Осень': [9, 10, 11]
    }
    for season in seasons:
        if month_number in seasons[season]:
            return season


def get_season_dict_tuple(month_number):
    """Возвращает время года, к которому относится месяц с номером month_number. Используется словарь с кортежами"""
    seasons = {
        (12, 1, 2): 'Зима',
        (3, 4, 5): 'Весна',
        (6, 7, 8): 'Лето',
        (9, 10, 11): 'Осень'
    }
    for months in seasons:
        if month_number in months:
            return seasons[months]


def get_season_dict(month_number):
    """Возвращает время года, к которому относится месяц с номером month_number. Используется словарь"""
    seasons = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}
    return seasons[month_number]


def get_season_list(month_number):
    """Возвращает время года, к которому относится месяц с номером month_number. Используется список"""
    seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    return seasons[month_number - 1]


def print_season(month_number):
    """Несколькими способами вычисляет и выводит время года, к которому относится месяц с номером month_number"""
    print(f'Месяц {month_number} относится к времени года:')
    print(f'1 способ: {get_season_dict(month_number)}')
    print(f'2 способ: {get_season_list(month_number)}')
    print(f'3 способ: {get_season_dict_list(month_number)}')
    print(f'4 способ: {get_season_dict_tuple(month_number)}')


def get_errors():
    """
    Сравнивает работу разных способов и возвращает число несовпадений. В случае несовпадения результатов выводит месяц
    """
    error_count = 0
    for i in range(12):
        list = get_season_list(i + 1)
        dict = get_season_dict(i + 1)
        dict_list = get_season_dict_list(i + 1)
        dict_tuple = get_season_dict_tuple(i + 1)

        result = [list, dict, dict_list, dict_tuple]
        if len(set(result)) > 1:
            print(f'Ошибка для {i + 1} месяца')
            error_count += 1

    return error_count


def main():
    try:
        month_number = int(input('Введите номер месяца: '))
    except ValueError:
        print('Ошибка. Нужно ввести целое число!')
    except Exception:
        print('Неизвестная ошибка')
    else:
        if month_number > 12 or month_number < 1:
            print('Ошибка. Номер месяца должен быть в диапазоне от 1 до 12!')
        else:
            print_season(month_number)


main()
# print(f'Число ошибок: {get_errors()}')
