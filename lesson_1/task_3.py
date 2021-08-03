# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


# Вычисляет сумму через строки
def get_sum_str(number_str, count):
    result = 0
    for i in range(count):
        val_str = number_str * (i + 1)
        result += int(val_str)

    return result


# Вычисляет сумму - работает только для однозначных чисел (1 - 9)
def get_sum_number(number, count):
    result = 0
    val = 0
    for i in range(count):
        val += 10 ** i
        result += val

    return number * result


# Вычисляет сумму через сумму геометрической прогрессии - работает только для однозначных чисел (1 - 9)
# Формула получена так: каждое слагаемое - сумма 1, 2, 3 и т.д. до count слагаемых геометрической прогрессии c q = 10
# Сумму можно вычислить по формуле. Записать count слагаемых и выполнить преобразование
def get_sum_geometric(number, count):
    return number * (10 * (10 ** count - 1) / 9 - count) / 9


number_str = input('Введите число: ')
count = int(input('Введите число слагаемых: '))

print(f'Число {number_str}. Число слагаемых {count}. Сумма равна:')
print(f'1 способ: {get_sum_str(number_str, count)}')
print(f'2 способ: {get_sum_number(int(number_str), count)}')
print(f'3 способ: {get_sum_geometric(int(number_str), count)}')
