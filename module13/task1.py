def power_order(n):
    counter = 0
    metise = n
    if n > 1:
        while metise // 10 > 0:
            metise /= 10
            counter += 1
    else:
        while metise < 1:
            metise *= 10
            counter -= 1
    return metise, counter

x = float(input("Введите число: "))
if x > 0:
    metise, counter = power_order(x)
    print(f"Формат плавающей точки: x = {round(metise, abs(counter))} * 10 ** {counter}")
else:
    print("Неверный x!")
