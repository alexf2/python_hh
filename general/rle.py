def rle(str: str) -> str:
    left = 0
    right = 0
    prev_char = None

    res = ''

    def add_char():
        nonlocal res

        if prev_char:
            diff = right - left
            if diff > 0:
                res += f'{prev_char}{diff}'
            elif prev_char:
                res += prev_char

    while right < len(str):
        ch = str[right]

        if prev_char == ch:
            right += 1
        else:
            add_char()

            right += 1
            left = right
            prev_char = ch

    add_char()

    return res


for data in [
    'a',
    'aaaaa',
    'ab',
    'aa',
    'abb',
    'abbbc',
    'abbb',
    'aab',
    'abbb',
    'ababcccabaaaa',
        'accca']:
    print(data, ' --> ', rle(data))
