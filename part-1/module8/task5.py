left_border = int(input("Введите начало отрезка: "))
right_border = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

for x in range(right_border, left_border - 1, step):
    func_result = x**3 + 2 * x**2 - 4 * x + 1
    print(f"F({x}) =", func_result)
