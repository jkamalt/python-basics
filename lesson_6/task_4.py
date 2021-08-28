class Direction:
    """
    Перечисление для направлений поворота
    """
    Left, Right = range(2)


class Car:
    """
    Класс для описания объекта "автомобиль"
    """
    max_speed = 0

    def __init__(self, speed, color, name, is_police=False):
        """
        Конструктор класса
        :param speed: скорость
        :param color: цвет
        :param name: название
        :param is_police: True, если машина полицейская, иначе False
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        Описывает запуск машины
        """
        print('Машина поехала')

    def stop(self):
        """
        Описывает остановку машину
        """
        print('Машина остановилась')

    def turn(self, direction: int):
        """
        Описывает поворот машины
        :param direction: направление поворота, 0 - налево, 1 - направо
        """
        if direction == Direction.Left:
            print('Машина повернула налево')
        elif direction == Direction.Right:
            print('Машина повернула направо')
        else:
            print('Направление поворота неизвестно')

    def show_speed(self):
        """
        Выводит на экран скорость машины
        """
        print(f'Скорость машины: {self.speed}')

    def check_over_speed(self):
        """
        Преверяет скорость машины на превышение максимальной скорости.
        В случае превышения выводит предупреждающее сообщение на экран
        """
        if self.speed > self.max_speed:
            print(f'Превышение скорости! Максимальная допустимая скорость {self.max_speed} км/ч')


class TownCar(Car):
    """
    Класс для описания объекта "городской автомобиль"
    """
    max_speed = 60

    def show_speed(self):
        super().show_speed()
        super().check_over_speed()


class WorkCar(Car):
    """
    Класс для описания объекта "рабочий автомобиль"
    """
    max_speed = 40

    def show_speed(self):
        super().show_speed()
        super().check_over_speed()


class SportCar(Car):
    """
    Класс для описания объекта "спортивный автомобиль"
    """


class PoliceCar(Car):
    """
    Класс для описания объекта "полицейский автомобиль"
    """


def show_car_info(car: Car):
    """
    Выводит значения атрибутов объекта car на экран
    :param car: объект класса Car
    """
    print(f'Скорость: {car.speed}, цвет: {car.color}, название: {car.name}, это полицейская машина: {car.is_police}')


def call_car_methods(car: Car, direction: int):
    """
    Вызывает методы объекта car
    :param car: объект класса Car
    :param direction: направление поворота, 0 - налево, 1 - направо
    :return:
    """
    car.go()
    car.turn(direction)
    car.stop()
    car.show_speed()


def main():
    town_car = TownCar(60, 'Черный', 'Toyota')
    show_car_info(town_car)
    call_car_methods(town_car, Direction.Left)

    town_car.speed = 80
    town_car.show_speed()

    print('\n')
    work_car = WorkCar(40, 'Черный', 'Volkswagen')
    show_car_info(work_car)
    call_car_methods(work_car, Direction.Right)

    work_car.speed = 60
    work_car.show_speed()

    print('\n')
    sport_car = SportCar(100, 'Красный', 'Ferrari')
    show_car_info(sport_car)
    call_car_methods(sport_car, 0)

    print('\n')
    police_car = PoliceCar(60, 'Белый', 'Ford', True)
    show_car_info(police_car)
    call_car_methods(police_car, 10)


main()
