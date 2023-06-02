# границы букв:
ENG_START = ord('a')
ENG_END = ord('z')
RUS_START = ord('а')
RUS_END = ord('я')


def decode(c, move):
    is_upper = False
    is_eng = False

    # Устанавливаем параметры буквы:
    if c.isupper():
        is_upper = True
    if ENG_START <= ord(c.lower()) <= ENG_END:
        is_eng = True

    c = c.lower()
    new_c = ord(c) - move
    while True:
        if is_eng and new_c < ENG_START:
            new_c += 26
        elif not is_eng and new_c < RUS_START:
            new_c += 32
        else:
            break
    if is_upper:
        return chr(new_c).upper()
    else:
        return chr(new_c)


def encode(c, move):
    is_upper = False
    is_eng = False

    # Устанавливаем параметры буквы:
    if c.isupper():
        is_upper = True
    if ENG_START <= ord(c.lower()) <= ENG_END:
        is_eng = True

    c = c.lower()
    new_c = ord(c) + move
    while True:
        if is_eng and new_c > ENG_END:
            new_c -= 26
        elif not is_eng and new_c > RUS_END:
            new_c -= 32
        else:
            break
    if is_upper:
        return chr(new_c).upper()
    else:
        return chr(new_c)
