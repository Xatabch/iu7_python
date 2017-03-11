import functions as fc
a = -2#int(input("Введите начало отрезка: "))
b = 5#int(input("Введите конец отрезка: "))
h = 0.5#float(input("Введите шаг: "))
n = 10#int(input("Введите максимальное количество итерраций: "))
eps1 = 0.1#float(input("Введите первую точность: "))
eps2 = 0.01#float(input("Введите вторую точность: "))

#Шаги.
while a < b:
    sled_znach = a
    pred_znach = sled_znach
    sled_znach = pred_znach + h
    a += h
    #Проверка на наличие корней на данном отрезке.
    if ((fc.func(pred_znach) < 0) and (fc.func(sled_znach) > 0)) or ((fc.func(pred_znach) > 0) and (fc.func(sled_znach) < 0)):
        x0 = pred_znach
        x1 = sled_znach
        proverca_1 = fc.second_proizv(x0)
        proverca_2 = fc.second_proizv(x1)
        number_of_root = 0
#РАЗОБРАТЬСЯ С ДУБЛИРОВАНИЕМ ЦИКЛОВ!!!!!
        if proverca_1:
            #print("proverca_1")
            #print(proverca_1, proverca_2)
            i = 0
            x2 = fc.newton1(x0)
            while abs(x2-x0) > eps1:
                x2 = x0
                x0 = fc.newton1(x0)
                #print(x0,x2)
                i += 1
                if i >= n:
                    break
            #print(x0)
            #print(pred_znach, sled_znach)
            number_of_root += 1
            function = fc.func(x0)
            fc.vivod(x0, number_of_root, pred_znach, sled_znach, function, i)
        else:
            #print("proverca_2")
            #print(proverca_1, proverca_2)
            i = 0
            x2 = fc.newton1(x1)
            while abs(x2-x1) > eps1:
                x2 = x1
                x1 = fc.newton1(x1)
                #print(x1,x2)
                i += 1
                if i >= n:
                    break
            #print(x1)
            number_of_root += 1
            function = fc.func(x1)
            fc.vivod(x1, number_of_root, pred_znach, sled_znach, function, i)
