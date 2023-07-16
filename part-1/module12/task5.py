def count_letters(text, k, n):
    print(f"Количество цифр {k}:", text.count(str(k)))
    print(f"Количество букв {n}:", text.count(n.lower()))

text = input("Введите текст: ")
k = int(input("Какую цифру ищем? "))
n = input("Какую букву ищем? ")
count_letters(text, k, n)