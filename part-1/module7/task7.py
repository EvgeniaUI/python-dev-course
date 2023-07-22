
N = int(input("Введите число карточек: "))

sum_of_n = sum(range(1, N + 1))
sum_of_given_cards = 0

for i in range(1, N):
    card_number = int(input("Введите номер оставшейся карточки: "))
    sum_of_given_cards += card_number

print("Номер пропавшей карточки:", sum_of_n - sum_of_given_cards)
