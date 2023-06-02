from Actions import decode

text = input('Введите текст сообщения для шифрования: ')
move = int(input('Введите сдвиг: '))
result = ''

for c in text:
    if not c.isalpha():
        result += c
        continue
    result += decode(c, move)

print(result)
