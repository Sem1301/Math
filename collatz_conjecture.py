def collatz1(a, b):
    """This collatz conjecture script shows the amount of steps needed,
    for a certain interval of integers to get to 1: (integer(i), steps(s))
    It only works for positive integers {1, 2, 3, ...}
    """
    if a < 1:
        a = 1
    for i in range(a, b + 1):
        y = 0
        x = i
        while i != 1:
            y += 1
            if i % 2 == 0:
                i /= 2
            else:
                i = 3 * i + 1
        yield x, y


def collatz(value):
    """This collatz conjecture script shows the amount of steps needed,
    for a certain interval of integers to get to 1: (integer(i), steps(s))
    It only works for positive integers {1, 2, 3, ...}
    """
    steps = 0
    i = value
    while i != 1:
        steps += 1
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
    return steps


if __name__ == '__main__':
    [print("Value: %5s -> Steps: %s" % (x, collatz(x))) for x in range(1, 101)]
