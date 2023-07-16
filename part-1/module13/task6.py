def find_x(D):
    x_b = 0
    x_e = 4
    middle = (x_b + x_e) / 2
    Dx = middle ** 3 - 3 * middle ** 2 - 12 * middle + 10
    while abs(Dx) > D:
        if D - Dx > 0:
            x_e = middle
        else:
            x_b = middle
        middle = (x_b + x_e) / 2
        Dx = middle ** 3 - 3 * middle ** 2 - 12 * middle + 10
    return middle



allowed_danger = float(input("Введите максимально допустимый уровень опасности: "))

print(f"Приблизительная глубина безопасной кладки: {find_x(allowed_danger)} м")

