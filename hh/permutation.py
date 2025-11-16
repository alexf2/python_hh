def perm(str_val):
    if not str_val or len(str_val) < 2:
        return -1

    digits = [int(v) for v in str_val]
    ll = len(digits)

    for i in range(ll - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            break

    if i < 0:
        return -1

    for j in range(ll - 1, -1, -1):
        if digits[j] < digits[i]:
            break

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)

    if (digits[0] == 0):
        return -1

    return int(''.join([str(v) for v in digits]))


for v in ['101', '531', '1281']:
    print(f'{v}: {perm(v)}')
