a = int(input("Введите ширину: "))
b = int(input("Введите длину: "))

a_symb = "-"
b_symb = "|"

first_row = b_symb + a_symb * a + b_symb
middle_row = b_symb + ' ' * a + b_symb + '\n'

square = first_row + '\n' + middle_row * (b - 2) + first_row

print(square)
