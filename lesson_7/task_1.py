class Matrix:
    """
    Класс для описания объекта "матрица"
    """

    def __init__(self, data):
        """
        Конструктор класса
        :param data: [[a11, a12, a13], [a21, a22, a23], ... ] список строк, где каждая строка тоже список
        """
        rows_sizes = set([len(row) for row in data])
        self.data = data if len(rows_sizes) == 1 else []

    def __str__(self):
        rows_str = ['\t'.join(map(str, row)) for row in self.data]
        return '\n'.join(rows_str)

    def __add__(self, other):
        if self.is_size_equal(other):
            result = [list(map(lambda x, y: x + y, self.data[i], other.data[i])) for i in range(len(self.data))]
            return Matrix(result)
        else:
            return None

    @property
    def rows_count(self):
        return len(self.data)

    @property
    def columns_count(self):
        return len(self.data[0]) if self.data else 0

    def is_size_equal(self, other):
        """
        Определяет имеют ли матрицы одинаковое количество строк и столбцов
        :param other: объект класса Matrix
        :return: True, если матрицы имеют одинаковое количество строк и столбцов, иначе False
        """
        return self.rows_count == other.rows_count and self.columns_count == other.columns_count


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'Матрица a:\n{a}')

    b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(f'Матрица b:\n{b}')

    c = Matrix([[1, 1, 1], [1, 1, 1]])
    print(f'Матрица c:\n{c}')

    d = Matrix([[1, 1], [1, 1], [1, 1]])
    print(f'Матрица d:\n{d}')

    e = Matrix([[1, 2, 3], [1], [1, 2]])
    print(f'Матрица e:\n{e}')

    print(f'Результат сложения матриц a + b:\n{a + b}')
    print(f'Результат сложения матриц a + c:\n{a + c}')
    print(f'Результат сложения матриц a + d:\n{a + d}')


main()
