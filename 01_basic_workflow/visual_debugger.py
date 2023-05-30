# Topics to cover:
# Introduce Python Tutor - https://pythontutor.com/visualize.html#mode=edit

a = 3
b = 2

c = a + b
print(c)


def add(a: int, b: int) -> int:
    return a + b


add_result = add(2, 3)
assert add_result == 5


def multiply_iterative(a: int, b: int) -> int:
    result = 0
    for _ in range(b):
        result += a
    return result


iterative_result = multiply_iterative(a, b)
assert iterative_result == 6


def multiply_generator(a: int, b: int) -> int:
    return sum(a for _ in range(b))


generator_result = multiply_generator(a, b)
assert generator_result == 6


def multiply_recursive(a: int, b: int, total: int = 0) -> int:
    if b == 0:
        return total
    return multiply_recursive(a, b - 1, total=total + a)


recursive_result = multiply_recursive(a, b)
assert recursive_result == 6


def multiply_recursive_ternary(a: int, b: int, total: int = 0) -> int:
    return total if b == 0 else multiply_recursive_ternary(a, b - 1, total=total + a)


ternary_result = multiply_recursive_ternary(a, b)
assert ternary_result == 6
