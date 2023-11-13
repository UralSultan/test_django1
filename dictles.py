# dict1 = {
#     "Sultan": {
#         "age": 26,
#         "full_name": "Uralbek Sultan",
#         "favorite_food": "plov",
#         "password": "123456",
#         "login": "Ural"
#     },
#     "Adil": {
#         "age": 25,
#         "full_name": "Adil Marat",
#         "favorite_food": "plov2",
#         "password": "123",
#         "login": "Adi"
#     }
# }
#
#
#
#
# dc = {
#     "name": "Sultan",
#     "last_name": "Ural",
#     "age": 23
# }
# my_dictionary = dict()
# print(my_dictionary)
#
# my_dictionary = dict(name="Sultan", age=26)
# print(my_dictionary)
#
# my_dictionary['pet'] = 'cat'
# print(my_dictionary)
#
# print(my_dictionary['name'])
#
# del my_dictionary['pet']
# print(my_dictionary)
#
# my_dictionary["name"] = 'Marat'
# print(my_dictionary)


# if 'car' in my_dictionary:
#     print("Yes it is")
# else:
#     print("no")

# dict1 = {
#     "name": "Sultan",
#     "last_name": "Uralbek",
#     "age": 26,
#     "pet": "cat",
#     "favor_food": "ramen"
# }
#
# dict1["car"] = "BMW"
# print(dict1)

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# for o in dict1.keys():
#     print(o)


# my_dictionary = dict()
# my_dictionary = dict(klass=7, school="N6", name="Marat")


# for k in dict1:
#     print(key)

# list2 = ['Sultan', 'Uralbek', 26, 'cat', 'ramen']
#
# for value in dict1.values():
#     print(value)

#
# for k, v in dict1.items():
#     print(f'{k} >>>>>> {v}')
#


# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())


# list2 = [1, 2, 3, 4, "sol", 'water', [5, 6, 7, 8]]
#
# a = list2[6][2]
#
# print(a)


# dict1 = {
#     "name": "Sultan",
#     "last name": "Uralbek",
#     "age": 26,
#     "pet": "cat",
#     "favor_food": "ramen"
# }
#
# del dict1["age"]
#
# print(dict1)
#
#
#
#
# # for value in dict1.values():
# #     print(value)
#
# # for key, value in dict1.items():
# #     print(f"{key} >>>>>>>>>>> {value}")
#
# """
# Задача 1. Необходимо написать программу, которая будет проверять есть ли введный ключ в словаре, если
# уже есть такой выдаем ошибку, если нет то говорим что можешь создать такой ключ."""
#
#
#
# """2) Сложение значений: Создайте словарь, представляющий собой учёт доходов разных людей за месяц.
# Посчитайте общий доход за месяц."""
# #
# # # incomes = {"Алиса": 1000, "Боб": 1500, "Клара": 800}
# # # total_income = sum(incomes.values())
# # # print("Общий доход за месяц:", total_income)
#
# """3) Изменение значений: Создайте словарь, представляющий собой информацию о студентах (имя, возраст, средний балл).
# Измените средний балл одного из студентов """
# #
# # # students = {"Иван": {"возраст": 20, "средний балл": 85}}
# # # students["Иван"]["средний балл"] = 90
#
# """4) Удаление элементов: Создайте словарь, содержащий перечень товаров и их цен. Удалите один из товаров из списка. """
#
# # products = {"яблоко": 1.0, "банан": 0.5, "апельсин": 1.2}
# # del products["яблоко"]
#
# """5) Перебор словаря: Создайте словарь, содержащий информацию о книгах (название, автор, жанр).
# Выведите все названия книг. """
# #
# # # books = {"Книга 1": "Автор 1", "Книга 2": "Автор 2", "Книга 3": "Автор 3"}
# # # for title in books.keys():
# # #     print(title)
# #
# """6) Подсчет количества элементов: Создайте словарь, содержащий список слов. Подсчитайте,
# сколько раз каждое слово встречается в списке. """
#
# # # words = ["apple", "banana", "apple", "cherry", "banana"]
# # # word_count = {}
# # # for word in words:
# # #     if word in word_count:
# # #         word_count[word] += 1
# # #     else:
# # #         word_count[word] = 1
# # # print(word_count)
# #
# """7) Словарь описаний товаров: Создайте словарь, представляющий собой товары в интернет-магазине.
# Каждый товар должен содержать информацию о названии, цене и описании. Затем выведите информацию о каждом товаре
# в формате "Название: [название], Цена: [цена], Описание: [описание]"."""
# #
# # # products = {
# # #     "товар1": {"название": "Монитор", "цена": 200, "описание": "27-дюймовый монитор"},
# # #     "товар2": {"название": "Ноутбук", "цена": 800, "описание": "Легкий и компактный ноутбук"},
# # #     "товар3": {"название": "Клавиатура", "цена": 50, "описание": "Мембранная клавиатура"}
# # # }
# # #
# # # for product, data in products.items():
# # #     print(f"Название: {data['название']}, Цена: {data['цена']}, Описание: {data['описание']}")
# #
# """8) Генератор паролей (без использования функций): Создайте словарь, в котором ключами являются логины пользователей,
# # а значениями - их исходные пароли. Запросите у пользователя логин и затем сгенерируйте случайный пароль для
# # этого пользователя (например, из букв и цифр). Замените исходный пароль в словаре на новый.
# #
# # !подсказка!
# # Используйте библеотеку string и random.
# # Так же вам необходимо найти как использовать функцию join()
# """
# #
# # import random
# # import string
# #
# # # users = {"user1": "password1", "user2": "password2", "user3": "password3"}
# # #
# # # login = input("Введите логин пользователя: ")
# # #
# # # if login in users:
# # #     characters = string.ascii_letters + string.digits
# # #     new_password = ''.join(random.choice(characters) for _ in range(8))
# # #     users[login] = new_password
# # #     print(f"Новый пароль для {login}: {new_password}")
# # # else:
# # #     print("Пользователь не найден.")
# #
# # """9) Сравнение словарей: Создайте два словаря с информацией о студентах (имя, возраст, средний балл).
# # Сравните их, выявив, есть ли студенты с одинаковыми именами в обоих словарях. """
# #
# # # students1 = {"Иван": 25, "Мария": 28, "Петр": 22}
# # # students2 = {"Мария": 29, "Анна": 27, "Петр": 22}
# # # common_names = set(students1.keys()) & set(students2.keys())
# #
# # """10) Вложенные словари: Создайте словарь, представляющий собой информацию о фильмах (название, год выпуска, режиссер).
# # Добавьте дополнительную информацию о жанре для каждого фильма. """
# #
# # # movies = {"Фильм 1": {"год выпуска": 2020, "режиссер": "Режиссер 1", "жанр": "Жанр 1"},
# # #           "Фильм 2": {"год выпуска": 2019, "режиссер": "Режиссер 2", "жанр": "Жанр 2"}}
# # # movies["Фильм 1"]["жанр"] = "Жанр 3"
# #
# #
#


"""Задача: имеются переменные:
name = “Джон”, last_name = “Доу”, age = 15, favorite_food = “Хот-Дог”
Необходимо составить след предложение с использованием форматирования строки:
«Мое имя Джон, фамилия Доу. Мне 15 лет, и моя любимая еда Хот дог.»
"""

# """ Задача: Напишите программу для нахождения радиуса круга
# Известна длинна окружности круга – 45
# Формула для решения этой задачи
# r = C / (2 * π)
# Где π (пи) - математическая константа, приближенно равная 3.14159.
#  """
#
#
# """
# Задача: Попросите пользователя ввести длины трех сторон треугольника: a, b и c.
# Затем используйте условные операторы, чтобы определить тип треугольника (равносторонний
# , равнобедренный, обычный) на основе введенных значений сторон.
# """
#
# a= int(input("a="))
# b= int(input("b="))
# c= int(input("c="))
#
# if a==b==c:
#     print("равносторонний треугольник")
#
# elif a==b or b==c or c==a:
#     print("равнобедренный треугольник")
#
# else:
#     print("обычный треугольник")


""" Напишите программу, которая удаляет все повторяющиеся элементы в списке.
Не используя функции.
"""

# n = [1, 2, 3, 4, 5, 3, 2, 2]
# a = []
# for i in n:
#     if i not in a:
#         a.append(i)
#     elif i in a:
#         continue
# print(a)


"""
Подсчет гласных в слове: пользователь вводит слово,
а затем программа подсчитывает количество гласных букв в слове.
"""

# a=input()
# b=['a','e','u','i','o','y']
# c=0
# for i in a:
#     if i in b:
#         c+=1
#     else:
#         continue
# print(c)

"Найти простые числа от 1 до 100"

# result = []
# for i in range(2, 100+1):
#     is_prime = True
#     for ii in range(2, int(i**0.5)+1):
#         if i%ii == 0:
#             is_prime = False
#             break
#     if is_prime:
#         result.append(i)
#
# print(result)

"""Задача: с помощью цикла for, подсчитать количество символов в след строке:
w_string = “Отличный день, для пробежки”.
"""
# w_string = 'Отличный день, для пробежки'
# b = 0
# for i in w_string:
#     b += 1
#
# print(b)


"""Задача: Программа просит ввод от пользователя время, в зависимости от этого времени
 программа вывод на экран какое сейчас время суток."""

# n = [22 , 23 , 24 , 1, 2 ,3 ,4 ,5 ]
# u = [6 , 7 , 8 , 9, 10 ]
# o= [11 , 12 ,13 ,14 ,15 ,16 ,17]
# p= [18,19,20,21]
#
#
# w=int(input("Введите время"))
# if w in u:
#     print("Утро")
# elif w in o:
#     print("День")
# elif w in p:
#     print("Вечер")
# elif w in n:
#     print("Ночь")


"""Задача: напишите программу которая находит среднее из 5 чисел которые ввел
 пользователь."""


# a = 12345
# res = 0
# a = str(a)
#
# for i in a:
#     res += int(i)
#
# print(res)


# def max_of_two(a, b):
#     if a > b:
#         print(f'{a} is max')
#         return a
#     elif a < b:
#         print(f"{b} is max")
#         return b
#     else:
#         print("equal")
#
#
# no = max_of_two(b=15, a=10) - 5
#
# print(no)
#
#
#
#
# def suu(a, b,c=0):
#     res = a + b + c
#     return res
#
#
# print(suu(5, 10, 10))





# def add(x, y):
#     res = x + y
#     return res
#
# add(2, 5)
#
#
# def func(a, b, c):
#     return a + b + c
#
#
# print(func(c=12, b=15, a=50))


# def d_of_circle(c):
#     res = c / 3.14
#     return res
#
#
# print(d_of_circle(20))







# for i in range(10):
#     print(i)


# print(add(7, 10))
#
# print(add(15, 19) - 20)


# def sum_list(a):
#     b = 0
#
#     for i in a:
#         b += i
#     return b
#
#
#
# lst = [1, 2, 3, 4, 5, 6]
#
# ls2 = [4, 5, 6, 7, 8, 8]
#
# ls = [1, 3, 5, 6, 7, 8, 5, 4,3]
#
# print(sum_list(lst))
# print(sum_list(ls2))





# inp = int(input())
# sum_check = 0
#
# while inp:
#     sum_check += inp % 10
#     inp = inp // 10
#
# print(sum_check)


# def sum_of_three(first, second, third):
#     res = first + second + third
#     return res
#
# def sultan(inp):
#     inp = str(inp)
#     sum_check = 0
#
#     for i in inp:
#         sum_check += int(i)
#     return sum_check
#
#
# a = sultan(12345)
# print(a)
#
#
#
#
#
#
# def func_a(a, b, c=0):
#     res = a + b + c
#     return res
#
# print(func_a(5, 6))



"""
1. Напишите функцию, которая принимает список в виде аргумента и возвращает самое большое число.

2. Создайте функцию, которая принимает список чисел в качестве аргумента и возвращает среднее значение этих чисел.
"""
#
# def average(a):
#     sum_list = 0
#     for i in a:
#         sum_list += i
#     res = sum_list / len(a)
#     print(res)
#
# list3 = [1, 2, 3, 4, 5, 6, 7]
# average(list3)
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list5 = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20]
# average(list4)
# average(list5)
"""
3. Напишите функцию, которая принимает строку и возвращает эту строку, перевернутую задом наперед.
"""
# def rev_name(a):
#     res = a[::-1]
#     print(res)
"""
4. Создайте функцию, которая принимает на вход число и проверяет, является ли оно четным.

Создайте функцию, которая принимает список чисел и возвращает список только четных чисел из исходного списка

Напишите функцию, которая принимает два списка и возвращает новый список, содержащий элементы, которые есть и в первом,
и во втором списке

Создайте функцию, которая принимает на вход строку и возвращает ее длину без использования встроенной функции len().

"""



# def max_in_list(numbers):
#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     print(max_number)
#
#
# lis1 = [1, 2, 3, 4, 5, 6, 7]
# max_in_list(lis1)



























