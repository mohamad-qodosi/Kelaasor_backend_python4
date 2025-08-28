from calculations import *

def add_list(a, b):
    return list(
        map(
            lambda x: add_numbers(x[0], x[1]),
            zip(a, b)
        )
    )

def sub_list(a, b):
    return list(
        map(
            lambda x: sub_numbers(x[0], x[1]),
            zip(a, b)
        )
    )

def mul_list(a, b):
    return list(
        map(
            lambda x: mul_numbers(x[0], x[1]),
            zip(a, b)
        )
    )

def div_list(a, b):
    return list(
        map(
            lambda x: div_numbers(x[0], x[1]),
            zip(a, b)
        )
    )

if __name__ == "__main__":
    print(add_list([1, 2, 3], [4, 5, 6]))
