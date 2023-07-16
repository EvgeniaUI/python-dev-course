
N = int(input("Введите количество учеников: "))
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0

for i in range(N):
    mark = int(input(f"Введите оценку ученика №{i + 1}: "))
    if mark == 3:
        cnt_3 += 1
    elif mark == 4:
        cnt_4 += 1
    else:
        cnt_5 += 1
if cnt_3 > cnt_4 and cnt_3 > cnt_5:
    print("Сегодня больше троечников")
elif cnt_4 > cnt_3 and cnt_4 > cnt_5:
    print("Сегодня больше хорошистов")
else:
    print("Сегодня больше отличников")
