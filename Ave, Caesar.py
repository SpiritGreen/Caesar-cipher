'''
На вход программе подается строка текста на английском языке,
в которой нужно зашифровать все слова. Каждое слово строки следует
зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
Гарантируется, что между различными словами присутствует один пробел.
'''

from Actions import encode

words_lst = input().split()
result = ''

for word in words_lst:
    # Рассчитаем сдвиг:
    move = 0
    for c in word:
        if c.isalpha():
            move += 1
    # Зашифруем слово:
    for c in word:
        if not c.isalpha():
            result += c
            continue
        result += encode(c, move)
    result += ' '

# Уберём лишние пробелы:
result = result.strip()
print(result)
