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
    x = x - func(x) / proizv_func(x)
    return x
def vivod(x, number_of_root, pred_znach, sled_znach, function, i, error):
    if x >= 0:
        print('{:>10} | {:<5}{:>5} | {:>10.7f} | {:<5.7f} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    else:
        print('{:>10} | {:<5}{:>5} | {:<5.7f} | {:<5.7f} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
    
