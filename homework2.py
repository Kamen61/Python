# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11


# number = input('Введите число : ')
# sum = 0
# for i in number:
#     if (i != ",") & (i != "-"):
#         sum = sum + int(i)
# print(sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# digit=int(input('введите число'))
# sum=1
# for i in range(1,digit):
#     sum=sum*i
#     print(sum , end=',')
# print(sum*digit)


# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.


# k=int(input('Введите число : '))
# count=1
# sum=0
# while count!=k+1:
#     sum=(1 + 1/count)**count
#     count+=1
#     print(round(sum,3))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# from posixpath import split
# from random import randint


# N=int(input('Введите размер массива : '))
# list=[]
# count=0
# while count!=N:
#     list.append(randint(-N,N))
#     count+=1
# print(list)
# index=input('Введите индексы через пробел : ').split()
# pow=1
# for i in range(0,len(index)):
#     pow=list[int(index[i])]*pow
# print(pow)



# Реализуйте алгоритм перемешивания списка.

# from random import randint

# list=[0,1,2,3,4,5,6,7,44,2233,455]
# swap=0
# for i in range(0,len(list)-1):
#     index=randint(0,len(list)-1)
#     swap=list[i]
#     list[i]=list[index]
#     list[index]=swap
# print(list)

# или


# import random

# list=[0,1,2,3,4,5,6,7,44,2233,455]
# random.shuffle(list)
# print(list)