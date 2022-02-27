class Stationery:
    """
    Класс для описания объекта "канцелярская принадлежность"
    """

    def __init__(self, title):
        """
        Конструктор класса
        :param title: название
        """
        self.title = title

    def draw(self):
        """
        Метод отрисовки
        """
        print('Запуск отрисовки')


class Pen(Stationery):
    """
    Класс для описания объекта "ручка"
    """

    def draw(self):
        print(f'{self.title} рисует ручкой')


class Pencil(Stationery):
    """
    Класс для описания объекта "карандаш"
    """

    def draw(self):
        print(f'{self.title} рисует карандашом')


class Handle(Stationery):
    """
    Класс для описания объекта "маркер"
    """

    def draw(self):
        print(f'{self.title} рисует маркером')


def main():
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')

    pen.draw()
    pencil.draw()
    handle.draw()


main()
