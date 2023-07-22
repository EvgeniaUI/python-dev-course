
def digits_count(n):
    return len(str(n))
def modified(n, number):
    count = digits_count(n)
    if count < 3 and number == 1:
        print("В первом числе меньше трёх цифр.")
    elif count < 4 and number == 2:
        print("Во втором числе меньше четырёх цифр.")
    else:
        last_digit = n % 10
        first_digit = n // 10 ** (count - 1)
        between_digits = n % 10 ** (count - 1) // 10
        return last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return n


def main():
    first_n = int(input("Введите первое число: "))
    new_first = modified(first_n, 1)

    second_n = int(input("\nВведите второе число: "))
    new_second = modified(second_n, 2)

    print('\nСумма чисел:', new_first + new_second)

main()