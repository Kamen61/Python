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




with open('exe5file1.txt','r') as f1:
    file1=f1.readline()
    file1=file1.split(' ')
with open('exe5file2.txt','r') as f2:
    file2=f2.readline()
    file2=file2.split(' ')

print(file1)
print(file2)

for i in file1:
    index_file1=i.find('x')
    if index_file1!=-1:
    
        print(index_file1)
    print(i)        


# Использовать find  для поиска эелементов в списке с степенью и без нее 
# Искать из одного списка число с такой же степенью как и во втором списке , после чего удалять его из второго списка 
# использовать split для того чтобы разделять эелемент списка на степень и число инкремент 

# list_file1=[]
# for i in range(len(file1)):
#     list_file1.append(file1[i])

# print(list_file1)

# list_file2=[]
# for i in range(len(file2)):
#     list_file2.append(file2[i])

# print(list_file2)

        