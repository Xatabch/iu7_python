def func(x):
    return (x**2 - 3)#(x**3 + 4*x - 3)
def proizv_func(x):
    return (2 * x)#(3 * x ** 2 + 4)
def second_proizv(x):
    function = (x**2 - 3)#x ** 3 + 4 * x - 3
    second = 2 #6 * x
    result = function * second
    if result > 0:
        return 1
    else:
        return 0
def newton1(x):
    x = x - func(x) / proizv_func(x)
    return x
def vivod(x, number_of_root, pred_znach, sled_znach):
    if x > 0:
        print('{:>10} | {:<5}{:>5} | {:>10.7f} |'.format(number_of_root, pred_znach, sled_znach, x))
    else:
        print('{:>10} | {:<5}{:>5} | {:<5.7f} |'.format(number_of_root, pred_znach, sled_znach, x))
    