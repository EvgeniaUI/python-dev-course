
even_negative_cnt = 0
for i in range(10):
    n = int(input("Введите номер должника: "))
    if n < 0 and n % 2 == 0:
        even_negative_cnt += 1
print("Одновременно чётные и положительные:", even_negative_cnt)
