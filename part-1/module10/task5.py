N = int(input("Введите количество чисел: "))
max_sum = 0
max_number = 0
for i in range(N):
    number = int(input("Введите число: "))
    list_number = list(map(int, list(str(number))))
    if sum(list_number) > max_sum:
        max_sum = sum(list_number)
        max_number = number
print("Число с максимальной суммой цифр:", max_number)
