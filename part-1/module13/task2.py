def maximum_of_two(x, y):
    return (x > y) * x + (x < y) * y

def maximum_of_three(x, y, z):
    return (maximum_of_two(x, y) > z) * maximum_of_two(x, y) + (maximum_of_two(x, y) < z) * z

print("Введите 3 числа в строку:")
x, y, z = map(float, input().split())

print("Максимум:", maximum_of_three(x, y, z))