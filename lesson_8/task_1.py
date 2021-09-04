class Date:
    """
    Класс "дата"
    """

    def __init__(self, day, month, year):
        """
        Конструктор класса
        :param day: день
        :param month: месяц
        :param year: год
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year:02}'

    @classmethod
    def create_from_string(cls, date_str):
        """
        Создает новый объект класса Date из строки вида "день-месяц-год"
        :param date_str: строка вида "день-месяц-год"
        :return: объект Date
        """
        return cls(*Date.parse_date(date_str))

    @staticmethod
    def is_date_valid(date_str):
        """
        Проверяет компоненты строки вида "день-месяц-год" на корректность
        :param date_str: строка вида "день-месяц-год"
        :return: True, если все компоненты строки корректные, иначе False
        """
        day, month, year = Date.parse_date(date_str)
        return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000

    @staticmethod
    def parse_date(date_str):
        """
        Преобразует строку вида "день-месяц-год" в список чисел [день, месяц, год]
        :param date_str: строка вида "день-месяц-год"
        :return: список чисел [день, месяц, год]
        """
        return map(int, date_str.split('-'))


def main():
    date_1 = Date(1, 1, 2021)
    date_2 = Date.create_from_string('02-01-2021')
    print(date_1)
    print(date_2)

    print(Date.is_date_valid('01-01-2021'))
    print(Date.is_date_valid('32-01-2021'))


main()
