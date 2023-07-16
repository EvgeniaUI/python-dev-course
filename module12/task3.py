def min_of_digits(number):
    return min(map(int,list(str(number))))

def max_of_digits(number):
    return max(map(int,list(str(number))))

def sum_of_digits(number):
    return sum(map(int,list(str(number))))

while 1:
    N = int(input("Введите число: "))
    action = int(input("Что нужно сделать?\n1 - найти сумму цифр числа,\n2 - найти минимальную цифру,\n3 - найти максимальную цифру: "))
    if action == 1:
        print("Сумма цифр =", sum_of_digits(N))
    if action == 2:
        print("Минимальная цифра =", min_of_digits(N))
    if action == 3:
        print("Максимальная цифра =", max_of_digits(N))

