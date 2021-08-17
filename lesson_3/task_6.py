# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.


def get_capitalize(word: str) -> str:
    """
    Возвращает слово с заглавной буквы
    :param word: Исходное слово
    :return: Исходное слово с заглавной буквы
    """
    return word[0].upper() + word[1:]


def main():
    input_str = input('Введите слова, разделенные пробелами: ')
    words = input_str.split()

    result = ''
    for word in words:
        result += f'{get_capitalize(word)} '

    print(result)


main()
