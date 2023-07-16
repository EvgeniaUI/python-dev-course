educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите расходы на проживание: "))

lack_of_money = 0
for month in range(0, 10):
    lack_of_money += expenses - educational_grant
    print(f"{month + 1}'й месяц: траты {expenses}, не хватает {lack_of_money} рублей")
    expenses *= 1 + 3 / 100

print(f"Нужно попросить у родителей {lack_of_money}")
