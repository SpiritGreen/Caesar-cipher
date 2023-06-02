from Actions import decode

text = input("Введите текст: ")

for i in range(1, 26):
    result = ''
    for c in text:
        if not c.isalpha():
            result += c
            continue
        result += decode(c, i)
    print(f'#{i}: {result}')
