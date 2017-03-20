#Морозов Иван, ИУ7-24
#1-ая ч.Уточнение корней методом Ньютона
#2-ая ч.Вывод графика функции.

#Импорт файла с функциями
import functions as fc


#Библиотеки
import math as m
import pylab
from matplotlib import mlab
import scipy.optimize as sp
import scipy.misc as misc

#Ввод данных
a,b =map(float,input('Введите начало и конец отрезка: ').split())
d = a
c = b
h = float(input("Введите шаг: "))
n = int(input("Введите максимальное количество итерраций: "))
eps1 = float(input("Введите точность: "))
error = 0
number_of_root = 0
print("""
         Коды ошибок:
         0 - нет ошибок
         1 - превышено максимальное число итерраций
         2 - для данной функции метод работает ошибочно
         (Касательная вышла за пределы отрезка.)
""")
print('{:>10s} | {:<5s}{:>5s}| {:^10s} | {:^9s} | {:^5s} | {:^5} |'.format('№', 'X(n)',
                                                    'X(n+1)', 'X', 'f(X)', 'n', 'err'))
print('         ---------------------------------------------------------')

#Первая часть задания(Уточнение корня).
while a <= b:
    sled_znach = a
    pred_znach = sled_znach
    sled_znach = pred_znach + h
    a += h
    #Проверка на наличие корней на данном отрезке.
    if (fc.func(pred_znach) * fc.func(sled_znach) < 0) or (fc.func(pred_znach) == 0) \
       or (fc.func(sled_znach) == 0):
        x0 = pred_znach
        x1 = sled_znach
        proverca_1 = fc.second_proizv(x0)
        proverca_2 = fc.second_proizv(x1)
        #Уточнение корней.
        #print(proverca_1,proverca_2)
        if proverca_1:
            number_of_root += 1
            fc.utochnenie(proverca_1,x1,eps1,n,number_of_root,pred_znach,sled_znach,error,c,h,d)
            error = 0
        elif proverca_2:
            number_of_root += 1
            fc.utochnenie(proverca_1,x1,eps1,n,number_of_root,pred_znach,sled_znach,error,c,h,d)
            error = 0
        elif not proverca_1 and not proverca_2:
            number_of_root += 1
            #print(x0,x1)
            fc.utochnenie(proverca_1,x0,eps1,n,number_of_root,pred_znach,sled_znach,error,c,h,d)
                

#Вторая часть задания.
fc.graph(d,c)
