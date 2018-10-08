from functools import lru_cache


@lru_cache()
def fib(n):
    if n < 0:
        raise ValueError()
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
