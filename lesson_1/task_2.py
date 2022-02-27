#  Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк.


import time


# 1 способ - с использованием арифметических операций. Начинаем с часов
def convert_arithmetic(seconds):
    # Убирает сутки из введенного количества секунд
    seconds = seconds % (24 * 3600)

    # Вычисляет количество часов и остаток
    hours = seconds // 3600
    seconds %= 3600

    # Вычисляет количество минут и остаток
    minutes = seconds // 60
    seconds %= 60

    return f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}'


# 2 способ - с использованием метода divmod (возвращает частное и остаток от деления).
# Также отличие - начинаем наоборот с секунд
def convert_divmod(seconds):
    # Убирает сутки из введенного количества секунд
    seconds = seconds % (24 * 3600)

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}'


# 3 способ - с использованием метода strftime
def convert_strftime(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))


seconds = int(input('Введите время в секундах: '))

print(f'{seconds} секунд в формате чч:мм:сс без учета суток:')
print(f'1 способ: {convert_arithmetic(seconds)}')
print(f'2 способ: {convert_divmod(seconds)}')
print(f'3 способ: {convert_strftime(seconds)}')
