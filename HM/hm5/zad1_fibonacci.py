from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = {0: 0, 1: 1}
    def fibonacci(x: int) -> int:
        if x <= 0:
            return 0
        if x not in cache:
            cache[x] = fibonacci(x - 1) + fibonacci(x - 2)
        return cache[x]

    return fibonacci


fib = caching_fibonacci()
print(fib(100))
