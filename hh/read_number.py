digits = (
    'нуль',
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять')

tens = (
    'десять',
    'одиннадцать',
    'двенадцать',
    'тринадцать',
    'четырнадцать',
    'пятнадцать',
    'шестнадцать',
    'семнадцать',
    'восемнадцать',
    'девятнадцать')

rounds = (
    'двадцать',
    'тридцать',
    'сорок',
    'пятьдесят',
    'шетьдесят',
    'семдесят',
    'восемдесят',
    'девяносто')


def read_nuber(num: str) -> str:
    if not num:
        return ''

    val_num = int(num)
    if val_num < 1 or val_num > 99:
        raise ValueError('Not supported argument: should be in range 1 - 99')

    if val_num < 10:
        return digits[val_num]

    if val_num < 20:
        return tens[val_num % 10]

    rounds_part, rest_part = divmod(val_num, 10)
    return f'{rounds[rounds_part - 2]} {digits[rest_part]}' \
        if \
        rest_part else rounds[rounds_part - 2]


for v in range(1, 100):
    print(f'{v} --> {read_nuber(v)}')
