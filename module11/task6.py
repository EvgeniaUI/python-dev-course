from math import ceil

print("Введите местоположение коня:")
x0 = ceil(float(input()) * 10)
y0 = ceil(float(input()) * 10)


print("Введите местоположение точки на доске:")

x1 = ceil(float(input()) * 10)
y1 = ceil(float(input()) * 10)

print(f"Конь в клетке ({x0}, {y0}). Точка в клетке ({x1}, {y1})")

if (x0 - x1) ** 2 + (y0 - y1) ** 2 == 5 and x0 - x1 != 0 and y0 - y1 != 0:
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")
