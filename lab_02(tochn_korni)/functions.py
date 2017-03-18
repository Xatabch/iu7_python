import math as m

def func(x):
    return m.sin(x)#(x**2 - 3)#(x**3 + 4*x - 3)
def proizv_func(x):
    return m.cos(x)#(2 * x)#(3 * x ** 2 + 4)
def second_proizv(x):
    function = m.sin(x)#(x**2 - 3)#x ** 3 + 4 * x - 3
    second = -m.sin(x)#6 * x
    result = function * second
    if result > 0:
        return 1
    else:
        return 0
def newton1(x):
    if proizv_func(x) != 0:
        x = x - func(x) / proizv_func(x)
    return x
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
    
