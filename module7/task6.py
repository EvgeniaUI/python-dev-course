
print("Замечательные числа:")

for i in range(10, 100):
    dozens = i // 10
    units = i % 10
    if i == dozens * units * 3:
        print(i)
