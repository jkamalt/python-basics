from helper import try_parse


class NotNumberError(Exception):
    """
    Исключение возникающее, если элемент не является числом
    """
    pass


def main():
    numbers = []
    while True:
        try:
            print('Для выхода введите команду stop')
            input_str = input('Введите число: ')
            if input_str == 'stop':
                break
            number = try_parse(input_str, float)
            if number is None:
                raise NotNumberError('Введенная строка не является числом!')
            else:
                numbers.append(number)
        except NotNumberError as e:
            print(e)

    print(numbers)


main()
