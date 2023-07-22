hight = int(input("Введите глубину ямы: "))

space = "."

for i in range(hight, 0, -1):
    for number in range(hight, i - 1, -1):
        print(str(number), end="")
    print(space * (i - 1) * 2, end="")
    for number in range(i, hight + 1):
        print(str(number), end="")
    print()
