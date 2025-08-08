import time
from functools import lru_cache

# f(n) = f(n - 1) + f(n - 2)
# f(1) = 1
# f(2) = 2
def fibonacci_linear(n):
    fib = [1, 2]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[n - 1]

@lru_cache
def fibonacci_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return (
            fibonacci_recursive(n - 1)
            + fibonacci_recursive(n - 2)
    )

n = int(input())
t1 = time.time()
print(fibonacci_linear(n))
t2 = time.time()
print(fibonacci_recursive(n))
t3 = time.time()
print(t2 - t1)
print(t3 - t2)
