year = int(input("Введите год: "))

def SumDate(day):
    sum = 0
    for i in range(day+1):
        if i<10:
            sum = sum + i
        else:
            Days = str(i)
            ListDays = list(Days)
            sum = sum + int(ListDays[0]) + int(ListDays[1])
    return sum

try:
    if(year%100!=0 or year%400==0 and year%4==0):
        print("Високосный год")
        NumberSum = SumDate(31) * 7 + SumDate(30) * 4 + SumDate(29)
        print("Результат:", NumberSum)
    else:
        print("Невисокосный год")
        NumberSum = SumDate(31) * 7 + SumDate(30) * 4 + SumDate(28)
        print("Результат:", NumberSum)
except:
    print("Что-то не так")


