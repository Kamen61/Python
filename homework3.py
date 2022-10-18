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



# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать 
# случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место и выполнить 
# это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.


from random import randint


row=int(input('chislo row : '))
line=int(input('chislo line : '))
if (row*line)%2!=0:
    line+=1
result=[[0]*row for i in range(line)]

for j in range(line):
    print()
    for i in range(row):
        result[j][i]=randint(10,99)
        print(result[j][i],end=' ')


for i in range(line):
    swap=result[i][row-1]
    del result[i][row-1]
    result[i].insert(0,swap)

print()

for i in range(line):
    print()
    for j in range(row):
        print(result[i][j],end=' ')


