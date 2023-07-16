a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

max_number = (a > b) * a + (a < b) * b
print(max_number)
