def on_square(number):
    if number > 64 or number < 1:
        raise ValueError
    return 2**(number-1)


def total_after(number):
    if number > 64 or number < 1:
        raise ValueError
    return 2**number - 1
