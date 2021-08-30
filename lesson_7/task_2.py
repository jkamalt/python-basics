from abc import ABC, abstractmethod


class Clothes(ABC):
    """
    Класс для описания объекта "одежда с названием"
    """

    def __init__(self, title):
        """
        Конструктор класса
        :param title: название одежды
        """
        self.__title = title

    @property
    def title(self):
        return self.__title

    @abstractmethod
    def get_cloth_expense(self):
        """
        Вычисляет расход ткани на производство одежды
        :return: расход ткани
        """
        pass


class Coat(Clothes):
    """
    Класс для описания объекта "пальто"
    """

    def __init__(self, title, size):
        """
        Конструктор класса
        :param title: название пальто
        :param size: размер
        """
        super().__init__(title)
        self.size = size

    def get_cloth_expense(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    """
    Класс для описания объекта "костюм"
    """

    def __init__(self, title, length):
        """
        Конструктор класса
        :param title: название костюма
        :param length: рост
        """
        super().__init__(title)
        self.length = length

    def get_cloth_expense(self):
        return 2 * self.length + 0.3


def main():
    coat = Coat('Пальто', 50)
    costume = Costume('Костюм', 150)

    print(f'Расход ткани для предмета {coat.title}: {coat.get_cloth_expense()}')
    print(f'Расход ткани для предмета {costume.title}: {costume.get_cloth_expense()}')


main()
