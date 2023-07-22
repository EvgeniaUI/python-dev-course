a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))

sum_of_numbers = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sum_of_numbers += i
        counter += 1
print(f"Среднее арифметичское чисел из промежутка [{a}, {b}], кратных 3 =", sum_of_numbers / counter)
