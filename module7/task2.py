
salary = 0

for i in range(12):
    salary += int(input(f"Введите зарплату за {i + 1}'й месяц: "))

print("Средняя зарплата за год =", salary / 12)