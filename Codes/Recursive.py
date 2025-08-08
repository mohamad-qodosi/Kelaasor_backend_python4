import time
from functools import lru_cache
from typing import List
from pprint import pprint

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

def print_string(string: str, reverse: bool = False):
    """
    Practice problem 2:
    # input:
        python
    # output:
        P
        Y
        T
        H
        O
        N
    """
    if not reverse:
        print(string[0].upper())
        if len(string) != 1: print_string(string[1:])
    else:
        if len(string) != 1: print_string(string[1:])
        print(string[0].upper())


    """
    a   => a
    hi  => hi, ih
    ali => ali, ail, lia, lai, ila, ial
    [r, e, z, a] => [reza, reaz, rzea, rzae, raze, raez,
            zera, zear, zrea, zrae, zare, zaer,
            ezra, ezar, erza, eraz, earz, eazr,
            aerz, aezr, arez, arze, azre, azer]
    """
def permutation(chars: List[str], level=0, debug=False) -> List[str]:
    if debug:
        print("\t" * level, chars)
    if len(chars) == 1: return chars
    selected_char = chars[0]
    rest = chars[1:]
    rest_permutation = permutation(rest, level + 1)
    result = []
    for sub_permutation in rest_permutation:
        for index in range(len(sub_permutation) + 1):
            new_permutation = (
                sub_permutation[:index]
                + selected_char
                + sub_permutation[index:]
            )
            if debug:
                print("\t" * level,
                      f"'{sub_permutation[:index]}'",
                      f"'{selected_char}'",
                      f"'{sub_permutation[index:]}'",
                      "=>", new_permutation)
            result.append(new_permutation)
    if debug:
        print("\t" * level, "=>", result)
    return result


if __name__ == "__main__":
    # check_fibonacci()
    # print_string("python")
    pprint(permutation(["R", "E", "Z", "A"], debug=False))
    pprint(len(permutation(["R", "E", "Z", "A"])))