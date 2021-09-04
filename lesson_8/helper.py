def try_parse(input_str, parse_method):
    """
    Выполняет преобразование строки в число с помощью заданного метода
    :param input_str: строка, которую нужно преобразовать в число
    :param parse_method: метод преобразования строки в число
    :return: результат преобразования, None в случае ошибки пребразования
    """
    try:
        return parse_method(input_str)
    except ValueError as e:
        return None
