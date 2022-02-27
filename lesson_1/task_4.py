# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


# Находит самую большую цифру в числе с помощью аримфетических операций
def get_max_digit_arithmetic(number_str):
    number = int(number_str)
    max_digit = 0

    while number > 0:
        # Получает младший разряд числа
        number, digit = divmod(number, 10)
        if digit > max_digit:
            max_digit = digit

    return max_digit


number_str = input('Введите число: ')

print(f'Максимальная цифра в числе {number_str}:')
print(f'1 способ: {get_max_digit_arithmetic(number_str)}')
