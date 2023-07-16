
n = int(input("Введите число элементов последовательности: "))
row_sum = 0
for i in range(n):
    element = (-1)**i * 1 / 2**i
    print(f"{i}'й элемент = {element}")
    row_sum += element
print("Сумма ряда =", row_sum)
