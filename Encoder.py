from Actions import encode

text = input('Введите текст сообщения для расшифровки: ')
move = int(input('Введите сдвиг: '))
result = ''

for c in text:
    if not c.isalpha():
        result += c
        continue
    result += encode(c, move)

print(result)
