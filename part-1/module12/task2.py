def positive():
    return "Положительное"

def negative():
    return "Отрицательное"

def test(number):
    return positive() if number > 0 else negative()

N = int(input("Введите число: "))

print(test(N))
