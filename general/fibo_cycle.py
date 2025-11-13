import array


def fibo(n: int) -> list[int]:
    if n < 0:
        return []
    match n:
        case 0:
            return [0]
        case 1:
            return [0, 1]

    prev = 0
    curr = 1
    res = array.array('I', [0] * (n + 1))
    for i in range(2, n + 1):
        next = prev + curr
        res[i] = next
        prev = curr
        curr = next

    return res.tolist()


print(fibo(-10))
print()
for n in range(8):
    print(fibo(n), end='\r\n')
