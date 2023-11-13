# # list = [1, 2, 3, 4, 5]
# #
# # for i in list:
# # 	print(i)
# # else:
# # 	print("end")
# #
# # for x in range(1, 11):
# # 	for y in range(1, 11):
# # 		print(x, '*', y, '=', x * y, end="\n")
# # 	print()
# #
# # for i in range(1, 10):
# # 	if i == 5:
# # 		break
# # 	print(i)
# # else:
# # 	print("конец")
# #
# # s = 'hello'
# #
# # for i in s:
# # 	if i == 'e':
# # 		continue
# # 	print(i)
# #
# #
# #
# # num = 1
# # while num <= 10:
# #     if num == 7:
# #         print(num)
# #         num += 1








"""Задача: Напишите программу, которая выводит все четные числа от 1 до 20"""
for i in range(2, 20, 2):
    print(i)

""" Задача: Вычислите сумму всех чисел от 1 до 100. """

total = 0

for i in range(1, 101):
    total += i

print(total)

"""Задача: 1)Выведите таблицу умножения на 5 от 1.
           2)все 9 таблиц"""

for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x} * {y} = {x * y}")
    print()


for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

"""Задача: Напишите программу, которая находит факториал числа N (N вводится пользователем)."""

N = int(input("Введите число N: "))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(f"Факториал {N} равен {factorial}")


"""Задача: Проверьте, является ли заданное число простым (простое число делится только на 1 и само себя)."""

num = int(input("Введите число: "))
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print(f"{num} - простое число")
else:
    print(f"{num} - не простое число")

n = int(input())

for i in range(2, n):
    if n % i == 0:
        print("Число непростое", n)
else:
    print("ЧИсло простое", n)

"""Задача: Выведите первые 10 чисел Фибоначчи."""

n = 10
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

"""Задача: Напишите программу для вывода пирамиды из звездочек высотой 5 строк."""
# # for i in range(1, 6):
# #     print(" " * (5 - i) + "*" * (2 * i - 1))
"""Задача: Напишите программу для подсчета количества гласных букв в строке."""

"""I)	Напишите программу, вычисляющую сумму всех четных чисел от 0 до N (включительно). N - целое число, введенное пользователем.
Для решения используйте цикл for.

II) Напишите программу, которая выводит числа от 1 до T, где T - это введенное пользователем целое число, которое больше
или равно 35. Если при выводе будут встречаться числа: 7, 13, 21, 29, то их нужно пропустить. Для решения используйте цикл for,
условную конструкцию if-elif-else и оператор continue.

III) На вход поступает число N (пользователь вводит его с клавиатуры),
используя цикл for необходимо организовать вывод от 1 до N (включительно). Если число является четным,
то выводим его квадрат (число в степени 2). Если число нечетное, то выводим его куб (число в степени 3).

Пример: вход: 4 вывод: 1 в степени 3 = 1 2 в степени 2 = 4 3 в степени 3 = 27 4 в степени 2 = 16

# Напишите программу, которая в последовательности натуральных чисел определяет сумму чисел, кратных 6.
# Программа получает на вход количество чисел в последовательности, а затем сами числа.
# В последовательности всегда имеется число, кратное 6.
# Программа должна вывести одно число – сумму чисел, кратных 6.

# # Входные данные	Выходные данные
# # 3
# # 12                   6
# # 25
# # 6
# # '''
# #
# # for x in range(1, 10):
# #     for y in range(1, 10):
# #         print(f'{x} * {y} = {x * y}')
# #     print()
#
#
# # mdict = {"a": "a"}
# #
# # print(dict)
# #
# # my_dict = dict(sultan="uralbek", age=26, number="555666999")
# #
# #
# # my_dict['место работы'] = "google"
# # print(my_dict)
# #
# # my_dict['место работы'] = 'MUK'
# # print(my_dict)
# #
# #
# # check = input()
# #
# # for k in my_dict:
# #     if check in my_dict:
# #         print("ДАнный ключ уже используется, просьба придумать новый")
# #         break
# #     else:
# #         print("Данный ключ свободен, вы можете его использовать")
# #         break
#
# #
# employers = {
#     "Sultan": {
#         "age": 26,
#         "dep": "it",
#         "Years of Experience": 5,
#         "pet": "cat"
#     },
#     "Adil": {
#         "age": 25,
#         "dep": "dewops",
#         "Years of Experience": 20,
#         "pet": "dog"
#     }
# }
#
# for key, values in employers.items():
#     print(f"name of employer {key}")
#     print(f"working dep of employer is {values['dep']} ")
#     print(f"This employer is {values['age']} y.o.")
#     print(f"This employer has a {values['pet']}")
#     print()
#
# # print(employers.get("Marat", "55"))
# # print(employers)
# # print(my_dict)
# #
# # # Создание пустого словаря
# # empty_dict = dict()
# # print(empty_dict)  # {}
# #
# # # Создание словаря с начальными данными
# # my_dict = dict(имя="Иван", возраст=30)
# # print(my_dict)  # {'имя': 'Иван', 'возраст': 30}
# #
# # # Создание словаря с использованием списка кортежей
# # pairs = [("имя", "Иван"), ("возраст", 30)]
# # my_dict = dict(pairs)
# # print(my_dict)  # {'имя': 'Иван', 'возраст': 30}
# #
# #
# # print(my_dict.values())
# # print(my_dict.items())
# # print(my_dict.keys())
# #
# # values = my_dict.values()
# #
# # values_list = list(values)
# # print(values_list)
# #
# #
# #
# # items = my_dict.items()
# #
# # for key, value in items:
# #     print(f"Ключ: {key}, Значение: {value}")
#
# my_dict = {
#     "user": "Uralbek Sultan",
#     "age": 26,
#     "p_number": "0555888666",
#     2: "IUK"
# }
# #
# # my_dict["class"] = 6
# # print(my_dict)
# # my_dict["class"] = 8
# # print(my_dict)
# #
# # del my_dict["age"]
# # print(my_dict)
#
# # for key in my_dict:
# # #     print(key, my_dict[key])
# #
# # for keys, values in my_dict.items():
# # 	print(f"{keys} >>>> {values}")
#
# # check = input()
# #
# # for k in my_dict:
# #     if check in my_dict:
# #         print("Данный ключ уже используется, просьба придумать новый")
# #         break
# #     else:
# #         print("Данный ключ свободен, вы можете его использовать")
# #         break



#
# print(dict1["name"])
# dict1["car"] = "BMW"
# print(dict1)
#
# dict2 = dict(name="Adil", age=30)
# print(dict2)
#
# print(dict1.get("name"))
#
# del dict1["age"]
# print(dict1)
#
# if "name" in dict1:
#     print("Такой ключ уже используется")
# else:
#     print("Данный ключ свободен")
#
#
# for key in dict1:
#     print(key, dict1[key])
#
# print(dict1.values())
# print(dict1.keys())
# print(dict1.items())
#
#
# for k in dict1:
#     print(k)
#
# for value in dict1.values():
#     print(value)
#
#
# for key, value in dict1.items():
#     print(f"{key} >>>>>>> {value}")


dict3 = {
    "Sultan": {
        "nick_name": "Ural",
        "last name": "Uralbek",
        "age": 26,
        "pet": "cat",
        "favor_food": "ramen"
    },
    "Adil": {
        "nick_name": "Adi",
        "last name": "Sarse",
        "age": 25,
        "pet": "dog",
        "favor_food": "plov"
    }
}"""

