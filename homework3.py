# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3, 2, 3, 5, 9, 3, 3]
# result=0
# for i in range(1,len(list),2):
#     result+=list[i]
# print(result)





# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# result_list=[]
# lenght=len(list)
# half_lenght=int(lenght/2)
# if lenght%2==0:
#     for i in range(half_lenght):
#         result_list.append(list[i]*list[lenght-i-1])
# else:
#     for i in range(half_lenght):
#         result_list.append(list[i]*list[lenght-i-1])
#     result_list.append(list[half_lenght]*list[half_lenght])
# print(result_list)





# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


# while True:
#     entered=input('Введите несколько вещественных чисел через пробел : ').split( )
#     try:
#         list=list(map(float,entered))
#         for i in range(len(list)):
#             list[i]=round(list[i]%1,4)
#         print(max(list)-min(list))
#         break
#     except:
#         print('Ошибочное число, попробуйте еще раз')
#         continue







# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10




# a=3
# result=''
# while a!=1:
#     a1=int(a%2)
#     result+=str(a1)
#     a=int(a/2)
# result+=str(a)
# print(result[::-1])



# def binar(N):
#     if N >= 2:
#         binar(N // 2)
#     print(N % 2, end='')
# binar(8)







# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

def positive_fib(list_fib):
    num_1 = 0
    num_2 = 1
    for i in range(number + 1):
        list_fib.append(num_1)
        temp = num_1 + num_2
        num_1, num_2 = num_2, temp

def negative_fib(list_fib):
    num_1 = 1
    num_2 = -1
    for i in range(number):
        list_fib.insert(0, num_1)
        temp = num_1 - num_2
        num_1, num_2 = num_2, temp

number = int(input('Введите число: '))
fibonacci = []
negative_fib(fibonacci)
print(fibonacci)
positive_fib(fibonacci)
print(fibonacci)