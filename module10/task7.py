hight = int(input("Введите высоту пирамиды: "))
number = 1
for i in range(1, hight + 1):
    print("\t" * (hight - i), end="")
    for j in range(i):
        print(number, end="\t\t")
        number += 2
    print()
