print("У вас было 100 кг гречки")

month_number = 1
for i in range(100, 0, -4):
    print(f"Остаток гречки в {month_number}'й месяц:", i - 4)
    month_number += 1
