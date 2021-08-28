class Road:
    """
    Класс для описания объекта "дорога"
    """

    def __init__(self, length, width):
        """
        Конструктор класса
        :param length: длина - м
        :param width: ширина - м
        """
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, square_meter_mass, thickness):
        """
        Вычисляет массу асфальта в кг, необходимого для покрытия всего дорожного полотна
        :param square_meter_mass: масса асфальта для покрытия 1 кв м дороги толщиной 1 см - кг
        :param thickness: толщина полотна - см
        :return: требуемая масса асфальта - кг
        """
        return self._length * self._width * square_meter_mass * thickness


def main():
    length = 5000
    width = 20
    square_meter_mass = 25
    thickness = 5

    road = Road(length, width)
    asphalt_mass = road.calc_asphalt_mass(square_meter_mass, thickness)

    print(f'Параметры дорожного полотна: длина - {length} м, ширина - {width} м, толщина - {thickness} см, '
          f'масса асфальта для покрытия 1 кв м толщиной в 1 см - {square_meter_mass} кг')
    print(f'Требуемая масса асфальта: {asphalt_mass / 1000} т')


main()
