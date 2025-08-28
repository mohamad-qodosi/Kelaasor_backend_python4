def add_numbers(a, b):
    return a + b


def sub_numbers(a, b):
    return a - b


def mul_numbers(a, b):
    return a * b


def div_numbers(a, b):
    return a / b


if __name__ == "__main__":
    print("calculations.__name__:", __name__)
    print(add_numbers(3, 4), "= 7")
    print(sub_numbers(3, 4), "= -1")
    print(mul_numbers(3, 4), "= 12")
    print(div_numbers(3, 4), "= 0.75")
