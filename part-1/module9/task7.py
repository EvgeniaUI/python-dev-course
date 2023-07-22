word_to_decode = list(input("Введите слово для дешифровки: "))
print(*word_to_decode)
len_of_word = len(word_to_decode)
decode_word = []
for i in range(len_of_word):
    k = 2 * i
    if k < len_of_word:
        decode_word.append(word_to_decode[k])
    else:
        decode_word.append(word_to_decode[len_of_word - k - 1])

print(*decode_word)