#Напишите программу, которая принимает последовательность целых 
#чисел (в одной строке) и с помощь использования списочных выражений
#выводит только чётные числа.
#for x in range (30, 50): 
    #print (*range (30, 50)
    #print (x, end = ",")  #научится выводить числв в одну строку
   # if x/2  #научится дать задания чтобы программа поняла делется ли на цело X

#print (*range (30, 50))
#print (*range (30, 50))
    #print (x)
    #print (x, end = ",")  #научится выводить числв в одну строку
   # if x/2  #научится дать задания чтобы программа поняла делется ли на цело X
    # help(print)
from random import randint # вызвать функцию  randint из модуля random
for o in range (1, 20):  # начать цикл от 1 до 20
    x = (randint(0, 10)) # x= рандомному числу от 1 до 10
    if x %2 == 0:   # условия если чило х делится на 2 нацело то продолжать иначе искать другое число
        print(x, end = ',')  #значит выводить х