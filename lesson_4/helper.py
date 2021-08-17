def try_parse(input_str, parse_method):
    """
    Выполняет конвертацию строки в число с помощью заданного метода
    :param input_str: Строка, которую нужно сконвертировать в число
    :param parse_method: Метод конвертации
    :return: Результат конвертации, None в случае ошибки конвертации
    """
    try:
        return parse_method(input_str)
    except ValueError as e:
        return None
