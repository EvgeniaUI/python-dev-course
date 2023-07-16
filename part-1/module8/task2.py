number_of_clients = int(input("Введите количество должников: "))

outstanding = 0

for client_number in range(0, number_of_clients, 5):
    print("Должник с номером", client_number)
    outstanding += int(input("Сколько должны? "))
print("Общая сумма долга:", outstanding)