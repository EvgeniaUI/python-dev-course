hight = int(input("Введите высоту пирамиды: "))

symb = "#"
space = " "

for i in range(hight):
    print(space * (hight - i - 1) + symb * (2 * i + 1))
