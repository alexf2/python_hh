from typing import Generator


def fibo_gen(n: int) -> Generator[int, None, None]:
    if n < 0:
        return

    yield 0
    if n == 0:
        return

    yield 1
    if n == 1:
        return

    prev = 0
    curr = 1
    while n > 0:
        n -= 1
        next = prev + curr
        yield next
        prev = curr
        curr = next


print(fibo_gen(-10))
print()
for n in range(8):
    print(n, list(fibo_gen(n)), end='\r\n')
