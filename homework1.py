# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите дату : '))
# if a < 8 and a > 0:
#     if a < 6:
#         print('нет')
#     else:
#         print('да')
# else:
#     print('Введите корректное число')
#     exit

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('\nПроверяем выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z при помощи true и false')
# Boolean = [True, False]
# for x in Boolean:
#     for y in Boolean:
#         for z in Boolean:
#             if not (x and y and z):
#                 print(
#                     f' if x = {x}, y = {y}, z = {z} -> {not x or not y or not z}')


# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('\nВведите целое число по Х : '))
# y = int(input('Введите целое число по Y : '))

# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# else:
#     print('4')


# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

# num1=float(input('Введите первое число: '))
# num2=float(input('Введите второе число: '))
# act=input('Какое действие между числами: ')
# result=0
# if num1==0 or num2==0:
#     print('Деление на 0 !')
# else:
#     if act=='/':
#         result=num1/num2
#     elif act=='*':
#         result=num1*num2
#     elif act=='+':
#         result=num1+num2
#     elif act=='-':
#         result=num1-num2
#     elif act=='mod':
#         result=num1%num2
#     elif act=='div':
#         result=num1//num2
#     elif act=='pow':
#         result=num1**num2
#     print(result)



# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10



# line1 = [int(el) for el in input('Введите первую строчку массива : ').split()]
# line2 = [int(el) for el in input('Введите вторую строчку массива : ').split()]

# full_array=line1+line2
# a=1
# for i in range(len(full_array)-a):
#     for j in range(len(full_array)-i-a):
#         if full_array[j] > full_array[j+1]:
#             full_array[j], full_array[j+1] = full_array[j+1], full_array[j]
# count=0
# for i in range(len(full_array)):
#     if i<len(line1):
#         line1[i]=full_array[i]
#     else:
#         line2[count]=full_array[i]
#         count=count+1

# print(line1)
# print(line2)

