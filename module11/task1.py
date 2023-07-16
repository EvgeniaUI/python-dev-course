euro_to_dollar = 1.25
dollar_to_rub = 60.87

amount_eu = float(input("Введите сумму в евро: "))
amount_ru = amount_eu * euro_to_dollar * dollar_to_rub

print("Сумма в рублях:", amount_ru)
