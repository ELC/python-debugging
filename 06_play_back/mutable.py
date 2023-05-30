def add_value(xs: list[int], value: int) -> list[int]:
    xs.append(value)
    return xs


x = [1, 2, 3]
x_1 = add_value(x, 4)
x_2 = add_value(x, 5)
