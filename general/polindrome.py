def polindrome(str: str) -> bool:
    if len(str) < 2:
        return True

    left = 0
    right = len(str) - 1
    while left < right:
        if (str[left].casefold() != str[right].casefold()):
            return False
        left += 1
        right -= 1

    return True


for w in [
    '',
    'a',
    'aa',
    'abc',
    'казак',
    'Madam, I\'m Adam',
    'rotor',
    'level',
        'aba', 'Neveroddoreven']:
    print(w, polindrome(w))
