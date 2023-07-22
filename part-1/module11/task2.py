from math import log, exp

N = int(input("Введите количество чисел: "))

for i in range(N):
    x = float(input("Введите число: "))
    if x > 0:
        if x - int(x) > 0:
            x = int(x) + 1
        print(f"x = {x}\nlog({x}) = {log(x)}")
    else:
        if int(x) - x > 0:
            x = int(x) - 1
        print(f"x = {x}\nexp({x}) = {exp(int(x))}")
