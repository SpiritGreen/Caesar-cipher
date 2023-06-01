# границы букв:
eng_start = ord('a')
eng_end = ord('z')
rus_start = ord('а')
rus_end = ord('я')

# Ввод данных:
text = input('Введите текст сообщения: ')
move = int(input('Введите сдвиг: '))
result = ''

for c in text:
    if not c.isalpha():
        result += c
        continue

    is_upper = False
    is_eng = False

    # Устанавливаем параметры буквы:
    if c.isupper():
        is_upper = True
    if eng_start <= ord(c.lower()) <= eng_end:
        is_eng = True

    c = c.lower()
    new_c = ord(c) + move
    while True:
        if is_eng and new_c > eng_end:
            new_c -= 26
        elif not is_eng and new_c > rus_end:
            new_c -= 32
        else:
            break
    if is_upper:
        result += chr(new_c).upper()
    else:
        result += chr(new_c)

print(result)
