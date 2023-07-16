N = int(input("Введите количество чисел: "))
is_prime = 0
for i in range(N):
    element = int(input("Введите число: "))
    j = 2
    while j <= element**0.5:
        if element % j != 0:
            is_prime += 1
            break
        j += 1
print("Количество простых чисел в последовательности:", is_prime)
