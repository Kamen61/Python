# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
# from cmath import pi

# a=float(input('Введите точность вывода числа пи : '))
# count=0
# while a<1:
#     a*=10
#     count+=1
# print(round(pi,count))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def multipliers(num):
#     lst = []
#     for i in range(2, num):
#         if num % i == 0:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 lst.append(i)
#     return lst

# number = int(input('Введите натуральное число : '))
# print(multipliers(number))


# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# list=[1, 1, 2, 3, 4, 5, 2, 5]
# result=[]
# def non_recurring(list):
#     result=[]
#     for i in list:
#         if list.count(i)==1:
#             result.append(i)
#     return result

# print(non_recurring(list))


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint


# def polynomial(k):
#     inkrement_list = []
#     for i in range(0, k+1):
#         inkrement_list.append(randint(0, 100))
#     with open('result_exerciec4', 'a') as text:
#         text.write(f'{inkrement_list}\n')
#         for i in range(len(inkrement_list)):
#             if k!=1:

#                 if inkrement_list[i] != 1 and (inkrement_list[i] != 0  or i==len(inkrement_list)-1) :

#                     if i != len(inkrement_list)-1:
#                         text.write(f'{inkrement_list[i]}x^{k} + ')

#                     else:
#                         text.write(f'{inkrement_list[i]} = 0')

#                 else:
#                     text.write(f'x^{k} + ')
#             elif k==1 and inkrement_list[i]==1:
#                 text.write('х + ')
#             else:
#                 text.write(f'{inkrement_list[i]}х + ')
#             k -= 1
#         text.write('\n')

# polynomial(10)


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# with open('exe5file1.txt','r') as f1:
#     file1=f1.readline()
#     file1=file1.split(' ')
# with open('exe5file2.txt','r') as f2:
#     file2=f2.readline()
#     file2=file2.split(' ')

# print(file1)
# print(file1[18])
# print(file1[18].find('x'))
# print()
# print(file1[16])
# print(file1[16].find('x'))


# for i in file1:
#     index_file1=i.find('x')
#     if index_file1!=-1:

#         print(index_file1)
#     print(i)


# Использовать find  для поиска эелементов в списке с степенью и без нее
# Искать из одного списка число с такой же степенью как и во втором списке , после чего удалять его из второго списка
# использовать split для того чтобы разделять эелемент списка на степень и число инкремент

# Грустно признать но задача не получилась из за того что метод find не находил нужный элемент в строке (


# __________________________________________________________________________________________________________________________________
# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n=48
# result=[]
# count=2
# while n>1:
#     if n%count==0:
#         result.append(count)
#         n=n/count
#     else:
#         count+=1

# print(result)

# __________________________________________________________________________________________________________________________________
# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# sequence=[1,2,3,4,5,6,5,4,4,66,87,76,6,12]
# a=list(set(sequence))

# print(a)

# __________________________________________________________________________________________________________________________________
# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint

# polynomial=''
# k=12
# for i in reversed(range(2,k)):
#     polynomial+=f'{randint(0,100)}*x^{i} + '
# polynomial+=f'{randint(0,100)}*x + '
# polynomial+=f'{randint(0,100)} = 0 '
# print(polynomial)
# with open('polynomial.txt','w') as p:
#     p.write(polynomial)

# __________________________________________________________________________________________________________________________________
# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.


print('Решаем уровнение вида ax^2 + bx + c = 0')
while True:
    try:
        a = float(input('Введите первый коэфицент : '))
        b = float(input('Введите второй коэфицент : '))
        c = float(input('Введите третий коэфицент : '))
        Decriment = b**2-4*a*c
        print(f'Дискриминант равен {Decriment}')
        if Decriment == 0:
            х= -b / (2*a)
            print(f'у уровнения 1 корень . х = {х}')
        elif Decriment>0:
            x1 = round((-b+Decriment**0.5) / (2*a),3)
            x2 = round((-b-Decriment**0.5) / (2*a),3)
            print(f'у уровнения 2 корень . х1 = {x1} x2 = {x2}')
        else:
            print('У уровнения нет корней')
        break
    except:
        print('Ошибочное число, попробуйте еще раз')
        continue



# __________________________________________________________________________________________________________________________________
# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа.
# Тема чат-бота любая. Просьба - постараться не использовать простой одномерный список или простой одномерный словарь.
