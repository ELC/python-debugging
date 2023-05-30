def add_value(xs: list[int], value: int) -> list[int]:
    result = xs[:]
    result.append(value)
    return xs


x = [1, 2, 3]
x_1 = add_value(x, 4)
x_2 = add_value(x_1, 5)
