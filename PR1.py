
print("==========\nCalculator")
res = 0
print("Введите первое число: ")
a = int(input())
des = input("Выберите действие:\n 1 - сложение\n 2 - вычитание\n 3 - умножение\n 4 - деление\n 5 - степень(первое число - которое возводим, второе - его степень)\n 6 - остаток\n Действие: ")
print("Введите второе число: ")
b = int(input())

if des == '1':
    res = a + b
    print(f"Ответ: {res} ")
elif des == '2':
    res = a - b
    print(f"Ответ: {res} ")
elif des == '3':
    res = a * b
    print(f"Ответ: {res} ")
elif des == '4':
    if b != 0:
        res = a / b
        print(f"Ответ: {res} ")
    else:
        print("На 0 нельзя")
elif des == '5':
    res = a ** b
    print(f"Ответ: {res} ")
elif des == '6':
    if b !=0:
        res = a % b
        print(f"Ответ: {res} ")
    else:
        print("На 0 нельзя")
else:
    print("Вы что-то напутали")

while True:
    print("Введите следующее число: ")
    c = int(input())
    des = input("Выберите действие:\n 1 - сложение\n 2 - вычитание\n 3 - умножение\n 4 - деление\n 5 - степень(первое число - которое возводим, второе - его степень)\n 6 - остаток\n Действие: ")

    if des == '1':
        res = c + res
        print(f"Ответ: {res} ")
    elif des == '2':
        res = res - c
        print(f"Ответ: {res} ")
    elif des == '3':
        res = res * c
        print(f"Ответ: {res} ")
    elif des == '4':
        if c != 0:
            res = res / c
            print(f"Ответ: {res} ")
        else:
            print("На 0 нельзя")
    elif des == '5':
        res = res ** c
        print(f"Ответ: {res} ")
    elif des == '6':
        if c != 0:
            res = res % c
            print(f"Ответ: {res} ")
        else:
            print("На 0 нельзя")
    else:
        print("Вы что-то напутали")