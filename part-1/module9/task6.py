input_string = input("Введите данные о коровах: ")
list_of_input = list(input_string)

milk_counter = 0

for i in range(len(list_of_input)):
    if list_of_input[i] == 'a':
        milk_counter += 2 * (i + 1)

print("Всего молока за день:", milk_counter)
