import time
from functools import lru_cache
from typing import List

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

def check_fibonacci():
    n = int(input())
    t1 = time.time()
    print(fibonacci_linear(n))
    t2 = time.time()
    print(fibonacci_recursive(n))
    t3 = time.time()
    print(t2 - t1)
    print(t3 - t2)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_numbers(numbers_list: List[int]) -> int:
    """
    Practice problem 1:
        Write a function that takes a list of
        numbers as input and returns the sum
        of the numbers inside the list recursively.
        [5, 3, 7, 9, 2, 7] => ((((([] + 5) + 3) + 7) + 9) + 2) + 7
    """
    return (
            sum_of_numbers(numbers_list[:-1])
            + numbers_list[-1]
    ) if numbers_list else 0


"""

"""

if __name__ == "__main__":
    check_fibonacci()