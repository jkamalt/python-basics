# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


example_int = 10
example_str = 'Hello world'
example_float = 1.5
example_flag = True

print(example_int)
print(example_str)
print(example_float)
print(example_flag)

user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))
user_profession = input('Кто вы по профессии? ')
user_study_time = int(input('Сколько лет вы учились? '))

print(f'Привет, {user_name}! Вам {user_age} лет.')
print(f'Ваша профессия: {user_profession}. Вы учились {user_study_time} лет.')
