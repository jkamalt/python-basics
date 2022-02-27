from enum import Enum


class EquipmentType(Enum):
    """
    Перечисление для типов офисной техники
    """
    Printer = 0
    Scanner = 1
    Xerox = 2


class DepartmentType(Enum):
    """
    Перечисление для подразделений склада
    """
    Planet = 0
    Mercury = 1
    Mega = 2
    May = 3
    Central = 4


class PrinterType(Enum):
    """
    Перечисление для типов принтера
    """
    Laser = 0
    Jet = 1
    Matrix = 2


class Storage:
    """
    Класс "склад"
    """

    def __init__(self):
        """
        Конструткор класса
        """
        self.__storage_items = {item: 0 for item in list(EquipmentType)}
        self.__departments_items = {}
        for department in list(DepartmentType):
            self.__departments_items[department] = {item: 0 for item in list(EquipmentType)}

    def __str__(self):
        storage = ' '.join([f'{eq.name}: {count}' for eq, count in self.__storage_items.items()])
        departments = [f'{dep.name:10}: ' + ' '.join([f'{eq.name}: {count}' for eq, count in dep_data.items()])
                       for dep, dep_data in self.__departments_items.items()]
        return '\n'.join([storage] + departments)

    @property
    def storage_items_count(self):
        return sum(self.__storage_items.values())

    @property
    def departments_items_count(self):
        return sum([sum(department.values()) for department in self.__departments_items.values()])

    @property
    def total_items_count(self):
        return self.storage_items_count + self.departments_items_count

    def receive(self, equipment_type: EquipmentType, count: int):
        """
        Отвечает за прием оргтехники на склад. Увеличивает количество единиц соответствующего типа техники
        :param equipment_type: тип техники
        :param count: количество
        """
        errors = []
        if not isinstance(count, int):
            errors.append('Некорректные данные для параметра "количество"!')
        if not isinstance(equipment_type, EquipmentType):
            errors.append('Неизвестный тип техники!')

        if errors:
            print('\n'.join(errors))
            print('Невозможно принять технику!')
            return

        self.__storage_items[equipment_type] += count

    def transfer(self, department_type: DepartmentType, equipment_type: EquipmentType, count: int):
        """
        Отвечает за передачу оргтехники в определенное подразделение склада.
        Уменьшает количество единиц техники на главном складе, прибавляет это количество в подразделении склада
        :param department_type: подразделение склада
        :param equipment_type: тип передаваемой техники
        :param count: количество
        """
        errors = []
        if not isinstance(count, int):
            errors.append('Некорректные данные для параметра "количество"!')
        if not isinstance(equipment_type, EquipmentType):
            errors.append('Неизвестный тип техники!')
        if not isinstance(department_type, DepartmentType):
            errors.append('Неизвестное подразделение склада!')

        if errors:
            print('\n'.join(errors))
            print('Невозможно выполнить передачу техники!')
            return

        if self.__storage_items[equipment_type] >= count:
            self.__storage_items[equipment_type] -= count
            self.__departments_items[department_type][equipment_type] += count
        else:
            print('Количество единиц техники меньше, чем требуется. Невозможно выполнить передачу техники!')

    def get_storage_items_count(self, equipment_type: EquipmentType):
        """
        Возвращает количество единиц техники определенного типа на главном складе
        :param equipment_type: тип техники
        :return: количество на главном складе
        """
        return self.__storage_items.get(equipment_type)

    def get_department_items_count(self, department_type: DepartmentType, equipment_type: EquipmentType = None):
        """
        Возвращает количество единиц техники определенного типа в подразделении склада.
        Если тип техники не указан, то возвращается общее количество всех типов
        :param department_type: подразделение склада
        :param equipment_type: тип техники, если не указан, то возвращается общее количество всех типов
        :return: количество в подразделении склада
        """
        if not isinstance(department_type, DepartmentType):
            print('Неизвестное подразделение склада!')
            return
        if equipment_type is None:
            return sum(self.__departments_items[department_type].values())
        else:
            return self.__departments_items[department_type].get(equipment_type)


class OfficeEquipment:
    """
    Класс "оргтехника"
    """

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Printer(OfficeEquipment):
    """
    Класс "принтер"
    """

    def __init__(self, brand, model, printer_type, max_resolution, print_speed):
        super().__init__(brand, model)
        self.printer_type = printer_type
        self.max_resolution = max_resolution
        self.print_speed = print_speed

    def __str__(self):
        return f'Принтер {self.brand} {self.model}'


class Scanner(OfficeEquipment):
    """
    Класс "сканер"
    """

    def __init__(self, brand, model, optical_resolution, scanning_speed):
        super().__init__(brand, model)
        self.optical_resolution = optical_resolution
        self.scanning_speed = scanning_speed

    def __str__(self):
        return f'Сканер {self.brand} {self.model}'


class Xerox(OfficeEquipment):
    """
    Класс "ксерокс"
    """

    def __init__(self, brand, model, max_resolution, copy_speed):
        super().__init__(brand, model)
        self.max_resolution = max_resolution
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Ксерокс {self.brand} {self.model}'


def main():
    storage = Storage()
    storage.receive(EquipmentType.Printer, 20)
    storage.receive(EquipmentType.Scanner, 10)
    storage.receive(EquipmentType.Xerox, 5)

    storage.transfer(DepartmentType.Planet, EquipmentType.Printer, 5)
    storage.transfer(DepartmentType.Planet, EquipmentType.Scanner, 3)
    storage.transfer(DepartmentType.Planet, EquipmentType.Xerox, 2)

    print(storage)
    print(f'Количество единиц техники на складе: {storage.storage_items_count}')
    print(f'Количество единиц техники в подразделениях склада: {storage.departments_items_count}')
    print(f'Количество единиц техники всего (склад + подразделения): {storage.total_items_count}')

    print(f'Количество принтеров на складе: {storage.get_storage_items_count(EquipmentType.Printer)}')
    print(f'Общее количество единиц техники в подразделении Planet: '
          f'{storage.get_department_items_count(DepartmentType.Planet)}')


main()
