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


def read_rows(file_name: str) -> list:
    """
    Считывает данные из файла и возвращает результат в виде списка строк.
    :param file_name: имя файла
    :return: список строк
    """
    rows = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            rows.append(line.replace('\n', ''))
    return rows


def write_rows(file_name: str, rows: list):
    """
    Записывает список строк в файл. Данные записываются построчно.
    :param file_name: имя файла
    :param rows: список строк, которые будут записаны в файл
    """
    rows = '\n'.join(rows)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(rows)


def get_row_sum(row: str, parse_method):
    """
    Вычисляет сумму чисел в строке row, разделенных пробелами,
    которых удалось преобразовать в число методом parse_method.
    :param row: входная строка
    :param parse_method: метод преобразования строки в число
    :return: сумма чисел в строке, разделенных пробелами, которых удалось преобразовать в число
    """
    numbers = [try_parse(number, parse_method) for number in row.split()]
    return sum([number for number in numbers if number is not None])
