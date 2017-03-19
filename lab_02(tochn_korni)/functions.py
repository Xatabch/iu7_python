import math as m
import pylab
from matplotlib import mlab
import scipy.optimize as sp
import scipy.misc as misc

#Функция
def func(x):
    return (x**2 - 3)#m.sin(x)#(x**2 - 3)#(x**3 + 4*x - 3)

#Производная от функции
def proizv_func(x):
    return (2 * x)#m.cos(x)#(2 * x)#(3 * x ** 2 + 4)

#Определение числа от которого начинать уточнение.
def second_proizv(x):
    function = (x**2 - 3)#m.sin(x)#(x**2 - 3)#x ** 3 + 4 * x - 3
    second = 2#-m.sin(x)#6 * x
    result = function * second
    if result > 0:
        return 1
    else:
        return 0
#Формула метода Ньютона.
def newton1(x):
    if proizv_func(x) != 0:
        x = x - func(x) / proizv_func(x)
    return x

#Уточнение корня
def utochnenie(proverca,x,eps1,n,number_of_root,pred_znach,sled_znach,error):
    i = 0
    x2 = newton1(x)
    while abs(x2-x) > eps1:
        x2 = x
        x = newton1(x)
        i += 1
        if i >= n:
            error = 1
            break
    if i != 0:
        if pred_znach == 0 and func(pred_znach) == 0:
            x = 0.0
            i = 1
        function = func(x)
        viv = vivod(x, number_of_root, pred_znach, sled_znach, function, i, error)
        return viv

#Вывод результатов.
def vivod(x, number_of_root, pred_znach, sled_znach, function, i, error):
    if (x >= 0) and (function > 0):
        print('{:>10} | {:<5}{:>5} | {:>10.7f} | {:<5.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    elif (x <= 0) and (function < 0):
        print('{:>10} | {:<5}{:>5} | {:<5.7f} |{:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    elif (x <= 0) and (function > 0):
        print('{:>10} | {:<5}{:>5} | {:<5.7f} | {:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    elif (x >= 0) and (function < 0):
        print('{:>10} | {:<5}{:>5} | {:^11.7f}|{:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    elif (x == 0) and (function == 0):
        print('{:>10} | {:<5}{:>5} | {:^11.7f}| {:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))

def graph(xmin,xmax):
    xmin = -10
    xmax = 10
    h = abs(xmin - xmax)/100
    dx = 0.01

    xlist = mlab.frange(xmin, xmax, dx)
    ylist = [func(x) for x in xlist]

    x2 = []
    y2 = []
    x3 = []
    y3 = []
    
    for i in range(round(abs(xmin-xmax)/h*10)):
        if abs(misc.derivative(func,xmin+h*i/10)) <= h/10:
            x2.append(xmin+h*i/10)
            y2.append(func(xmin+h*i/10))
        if abs(misc.derivative(func,xmin+h*i/10,1,2)) <= h/10:
            x3.append(xmin+h*i/10)
            y3.append(func(xmin+h*i/10)) 

    rootsx = []
    rootscount = 0
    while xmin < xmax:
        if func(xmin) * func(xmin + h) < 0:
            rootsx.append(sp.ridder(func, xmin ,xmin+h))
            rootscount += 1
        xmin += h
        
    pylab.plot(xlist, ylist)
    pylab.grid(True)
    pylab.plot(rootsx,[0] * rootscount,'bo')
    pylab.plot(x2,y2,'ro')
    pylab.plot(x3,y3,'go')
    pylab.show()
