list_of_pirates = ["карамба", "Карамба"]
count_of_pirates = 10
count_of_true_pirates = 0
for i in range(count_of_pirates):
    pirate = input("Введите слово: ")
    if pirate in list_of_pirates:
        count_of_true_pirates += 1
print("Количество достойных пиратов на борту:", count_of_true_pirates)
