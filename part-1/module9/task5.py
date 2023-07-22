text = input("Введите текст: ")
words_list = text.split()
max_word = 0
for word in words_list:
    if len(word) > max_word:
        max_word = len(word)
print(f"Самое длинное слово, {max_word} букв")
