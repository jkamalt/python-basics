class Worker:
    """
    Класс для описания объекта "сотрудник"
    """

    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор класса
        :param name: имя сотрудника
        :param surname: фамилия сотрудника
        :param position: должность
        :param wage: оклад
        :param bonus: премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    """
    Класс описывающий объект "сотрудник с должностью"
    """

    def get_full_name(self) -> str:
        """
        Возвращает полное имя сотрудника в виде строки
        :return: полное имя сотрудника в виде строки
        """
        return f'{self.surname} {self.name}'

    def get_total_income(self) -> float:
        """
        Вычисляет доход сотрудника как оклад + премия
        :return: доход сотрудника
        """
        return self._income['wage'] + self._income['bonus']


def show_worker_info(worker: Worker):
    """
    Выводит значения атрибутов объекта worker на экран
    :param worker: объект класса Worker
    """
    print(f'Имя: {worker.name}, фамилия: {worker.surname}, должность: {worker.position}')


def main():
    worker = Position('Кот', 'Чеширский', 'Руководитель департамента IT', 400000, 50000)
    show_worker_info(worker)

    print(f'Полное имя сотрудника: {worker.get_full_name()}')
    print(f'Доход сотрудника: {worker.get_total_income()}')


main()
