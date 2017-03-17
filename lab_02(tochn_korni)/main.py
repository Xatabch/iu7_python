#Морозов Иван, ИУ7-24

import functions as fc
#import scipy.optimize as sp
#import scipy.misc as misc
#import matplotlib.pyplot as plt
#import numpy as np
#import math

a,b = map(float,input('Введите начало и конец отрезка: ').split())
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
""")
print('{:>10s} | {:<5s}{:>5s}| {:^10s} | {:^9s} | {:^5s} | {:^5} |'.format('№', 'X(n)', 'X(n+1)', 'X', 'f(X)', 'n', 'err'))
print('         ---------------------------------------------------------')

#Первая часть задания.
#Шаги.
while a < b:
    sled_znach = a
    pred_znach = sled_znach
    sled_znach = pred_znach + h
    a += h
    #print(fc.func(pred_znach),fc.func(sled_znach))
    #Проверка на наличие корней на данном отрезке.
    if ((fc.func(pred_znach) < 0) and (fc.func(sled_znach) > 0)) or ((fc.func(pred_znach) > 0) and (fc.func(sled_znach) < 0)):
        #print("Корень найден")
        x0 = pred_znach
        x1 = sled_znach
        proverca_1 = fc.second_proizv(x0)
        proverca_2 = fc.second_proizv(x1)
        number_of_root += 1
#РАЗОБРАТЬСЯ С ДУБЛИРОВАНИЕМ ЦИКЛОВ!!!!!
        if proverca_1:
            i = 0
            x2 = fc.newton1(x0)
            while abs(x2-x0) > eps1:
                x2 = x0
                x0 = fc.newton1(x0)
                #print(x0,x2)
                i += 1
                if i >= n:
                    error = 1
                    break
            function = fc.func(x0)
            fc.vivod(x0, number_of_root, pred_znach, sled_znach, function, i, error)
            error = 0
        else:
            i = 0
            x2 = fc.newton1(x1)
            while abs(x2-x1) > eps1:
                x2 = x1
                x1 = fc.newton1(x1)
                i += 1
                if i >= n:
                    error = 1
                    break
            function = fc.func(x1)
            fc.vivod(x1, number_of_root, pred_znach, sled_znach, function, i, error)
            error = 0

#2 Часть задания.
#print()
#def f(x):
#    return math.sin(x)#x**2 - 3
#a,b = map(float,input('Введите начало и конец отрезка: ').split())
#h = abs(b-a)/100
#x1 = np.arange (a,b,h/10)
#x2 = []
#y2 = []
#x3 = []
#y3 = []
#for i in range(round(abs(a-b)/h*10)):
#    if abs(misc.derivative(f,a+h*i/10)) <= h/10:
#        x2.append(a+h*i/10)
#        y2.append(f(a+h*i/10))
#    if abs(misc.derivative(f,a+h*i/10,1,2)) <= h/10:
#        x3.append(a+h*i/10)
#        y3.append(f(a+h*i/10))        
#rootsx = []
#rootscount = 0
#while a < b:
#    if f(a)*f(a+h) < 0:
#        rootsx.append(sp.ridder(f,a,a+h))
#        rootscount += 1
#    a += h
#plt.title('f(x) = $x^2$ - 3')
#plt.plot(x1,f(x1))
#plt.plot(rootsx,[0]*rootscount,'bo',label="Корни")
#plt.plot(x2,y2,'ro',label="Экстремумы")
#plt.plot(x3,y3,'go',label="Точки перегиба")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
#plt.show()
