
reverse_timer = int(input("Введите время в секундах: "))

for second in range(reverse_timer, 0, -1):
    print("Оставшееся время:", second)
    decision = int(input("Вы готовы забрать еду? 1 - да, 0 - нет: "))
    if decision == 1:
        print("Ваша еда готова, можете забрать")
        break
    elif second == 1:
        print("Ваша еда готова, осторожно горячo!")
