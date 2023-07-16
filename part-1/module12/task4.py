def reverse_number(number):
    return ''.join(list(str(number))[::-1])

N = int(input("Введите число: "))
print("Число наоборот:", reverse_number(N))
