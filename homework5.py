# 1) Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# a='Йцукфабв лдылвйщабв ьылфтоывтабв ыооы лзазкш цти т абвыввв, фыовтабвыокл'.split()
# b='абв'
# print(a)
# for i in reversed(range(len(a))) :
#     print(i)
#     if b in a[i] :
#         del a[i]

# print(' '.join(a))

# 2) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random
# def names(): 
#     print('Игра с конфетами \n'
#     'На столе лежит 2021 конфета \n'
#     'Можно брать оне более 28 конфет за раз \n'
#     'Все конфеты оппонента достаются сделавшему последний ход \n\n')
#     name_players=[]
#     for i in range(1,3):
#         name=input(f'Введите имя {i} игрока : ')
#         name_players.append(name)
#     return name_players

# def game(name):
#     amount_candy=2021
#     max_take=28
#     stap = random.getrandbits(1)
#     print('Произошла жеребьевка ')
#     while amount_candy>0:
#         if stap:
#             take_player=int(input(f'\nХодит {name[0]}\n'
#                 f'Сейчас на столе {amount_candy} конфет . Сколько вы хотите взять ?\n'))
#             if take_player not in range(1,max_take+1):
#                 print('Можно брать от 1 до 28 конфет за раз')
#                 continue
#             else:
#                 amount_candy-=take_player
#                 stap=0
#                 if amount_candy==0 or amount_candy<0:
#                     print(f'Победил {name[0]} !')
#         else:
#             take_player=int(input(f'\nХодит {name[1]}\n'
#                 f'Сейчас на столе {amount_candy} конфет . Сколько вы хотите взять ?\n'))
#             if take_player not in range(1,max_take+1):
#                 print('Можно брать от 1 до 28 конфет за раз')
#                 continue
#             else:
#                 amount_candy-=take_player
#                 stap=1
#                 if amount_candy==0 or amount_candy<0:
#                     print(f'Победил {name[1]} !')

# game(names())


#Игра с ботом 

# def next_move(balance, step):
#     return balance % (step + 1)

# print('Игра с конфетами \n'
#     'На столе лежит 2021 конфета \n'
#     'Можно брать оне более 28 конфет за раз \n'
#     'Все конфеты оппонента достаются сделавшему последний ход \n\n')
# name_player=input('Введите ваше имя : ')
# amount_candy=2021
# max_take=28
# stap = random.getrandbits(1)
# print('Произошла жеребьевка ')
# while amount_candy>0:
#     if stap:
#         take_player=next_move(amount_candy,max_take)
#         print(f'\nХодит компьютер \n'
#             f'Сейчас на столе {amount_candy} конфет . Компьютер взял {take_player} \n')
#         amount_candy-=take_player
#         stap=0
#         if amount_candy==0 or amount_candy<0:
#             print(f'Победил компьютер !')
#     else:
#         take_player=int(input(f'\nХодит {name_player}\n'
#             f'Сейчас на столе {amount_candy} конфет . Сколько вы хотите взять ?\n'))
#         if take_player not in range(1,max_take+1):
#             print('Можно брать от 1 до 28 конфет за раз')
#             continue
#         else:
#             amount_candy-=take_player
#             stap=1
#             if amount_candy==0 or amount_candy<0:
#                 print(f'Победил {name_player} !')


# 3) Даны два многочлена. Задача - сформировать их сумму.
#например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9


# 4) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encoding(text):
    res = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        res += str(count) + text[i]
        i += 1
    return res


file_1 = 'Exercise_05_start.txt'
with open(file_1, 'r') as f:
    string = f.readline()

result = encoding(string)

file_2 = 'Exercise_05_end.txt'
with open(file_2, 'w') as f:
    f.writelines(result)


# 36. Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную 
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 2, 8, 1 2, 3, 4, 1, 7] => [1, 4]


# from random import randint


# a=[1,2,3,6,7,8,9,10]
# result=[]
# for i in a:
#     prom=[]
#     while True:
#         if i in a:
#             prom.append(i)
#             i+=1
#         else:
#             result.append(prom)
#             break
# min_list=result[0]
# for i in result:
#     if len(i)>len(min_list):
#         min_list=i

# finish_list=[min_list[0],min_list[len(min_list)-1]]

# print(finish_list)

