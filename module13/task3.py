def reverse_number(number):
    return int(''.join(list(str(number))[::-1]))

n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))

n_reversed = reverse_number(n)
k_reversed = reverse_number(k)

print("Первое число наоборот:", n_reversed)
print("Второе число наоборот:", k_reversed)

print("Сумма:", n + k)
print("Сумма наоборот:", n_reversed + k_reversed)
