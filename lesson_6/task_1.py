from time import sleep


class TrafficLight:
    """
    Класс для описания объекта "светофор"
    """
    __states = [('Красный', 7), ('Желтый', 2), ('Зелёный', 10), ('Желтый', 2)]

    def running(self):
        """
        Переключает цвета светофора в бесконечном цикле
        """
        while True:
            for state in self.__states:
                print(state[0])
                sleep(state[1])


def main():
    traffic_light = TrafficLight()
    traffic_light.running()


main()
