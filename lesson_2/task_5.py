# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


def get_updated_rating(rating, number):
    """Добавляет новое число number в rating и сортирует в порядке невозрастания"""
    rating.append(number)
    return sorted(rating, reverse=True)


def main():
    rating = [7, 5, 3, 3, 2]

    try:
        number = int(input('Введите натуральное число: '))
        if number <= 0:
            raise ValueError()
    except ValueError:
        print('Ошибка. Нужно ввести натуральное число!')
    except Exception:
        print('Неизвестная ошибка')
    else:
        rating = get_updated_rating(rating, number)
        print(rating)


main()
