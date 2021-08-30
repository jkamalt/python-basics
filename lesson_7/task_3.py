from operator import add, sub, mul, truediv


class Cell:
    """
    Класс для описания объекта "клетка"
    """

    def __init__(self, cells_count: int):
        """
        Конструктор класса
        :param cells_count: количество ячеек клетки
        """
        self.cells_count = cells_count

    def __add__(self, other):
        """
        Результат сложения - новая клетка с числом ячеек, равным сумме ячеек двух исходных клеток
        :param other: клетка Cell
        :return: новая клетка Cell с числом ячеек, равным сумме ячеек двух исходных клеток
        """
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        """
        Результат вычитания - новая клетка с числом ячеек, равным разности ячеек двух исходных клеток.
        Если разность меньше 0, число ячеек новой клетки равно 0, и выводится предупреждающее сообщение
        :param other: клетка Cell
        :return: новая клетка Cell с числом ячеек, равным разности ячеек двух исходных клеток
        """
        diff = self.cells_count - other.cells_count
        if diff < 0:
            print('Разность количества ячеек двух клеток меньше 0! Число ячеек результата будет равно 0')
            return Cell(0)
        else:
            return Cell(diff)

    def __mul__(self, other):
        """
        Результат умножения - новая клетка с числом ячеек, равным произведению ячеек двух исходных клеток
        :param other: клетка Cell
        :return: новая клетка Cell с числом ячеек, равным произведенеию ячеек двух исходных клеток
        """
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        """
        Результат деления - новая клетка с числом ячеек,
        равным результату целочисленного деления ячеек двух исходных клеток
        :param other: клетка Cell
        :return: новая клетка Cell с числом ячеек, равным результату целочисленного деления ячеек двух исходных клеток
        """
        return Cell(round(self.cells_count / other.cells_count))

    def make_order(self, row_cells_count: int) -> str:
        """
        Возвращает строку, где ячейки клетки организованы по рядам по row_cells_count ячеек.
        Оставшиеся ячейки записываются в последний ряд.
        :param row_cells_count: количество ячеек в ряду
        :return: строка, где ячейки клетки организованы по рядам
        """
        rows_count, remainder = divmod(self.cells_count, row_cells_count)
        rows = ['*' * row_cells_count for _ in range(rows_count)]
        rows.append('*' * remainder)
        return '\n'.join(rows)


def check_work(operator, left: Cell, right: Cell, row_cells_count):
    result = operator(left, right)
    print(f'Число ячеек: {result.cells_count}')
    print(result.make_order(row_cells_count))
    print('\n')


def main():
    cell_1 = Cell(15)
    cell_2 = Cell(6)

    check_work(add, cell_1, cell_2, 5)
    check_work(sub, cell_1, cell_2, 5)
    check_work(sub, cell_2, cell_1, 5)
    check_work(mul, cell_1, cell_2, 20)
    check_work(truediv, cell_1, cell_2, 5)


main()
