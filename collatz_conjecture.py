import matplotlib.pyplot as plt
import numpy as np


# from math_functions import collatz


def collatz1(value):
    """TODO doc
    This collatz conjecture script shows the amount of steps needed,
    for a certain interval of integers to get to 1: (integer(i), steps(s))
    It only works for positive integers {1, 2, 3, ...}
    """
    steps = 0
    i = value
    while i != 1:
        steps += 1
        if i % 2 == 0:
            i /= 2
            yield steps, "left", int(i)
        else:
            i = 3 * i + 1
            yield steps, "right", int(i)


def collatz(value):
    """TODO doc
    This collatz conjecture script shows the amount of steps needed,
    for a certain interval of integers to get to 1: (integer(i), steps(s))
    It only works for positive integers {1, 2, 3, ...}
    """
    steps = 0
    i = value
    while i != 1:
        steps += 1
        if i % 2 == 0:
            i /= 2
            yield steps, "left", int(i)
        else:
            i = 3 * i + 1
            yield steps, "right", int(i)


def collatz_generator(start=1):
    num = start
    while True:
        yield num, collatz(num)
        num += 1


def collatz_plotter(min_value=1, max_value=100, dx=1):
    xas = np.arange(min_value, max_value, dx)
    yas = [collatz(x) for x in range(min_value, max_value)]

    fig, ax = plt.subplots()
    ax.plot(xas, yas)

    ax.set(xlabel='value', ylabel='steps',
           title='Collatz')
    ax.grid()

    fig.savefig("collatz%s.png")
    plt.show()


def max_steps():
    max = 0
    for x, y in collatz_generator(15733191):
        if y > max:
            max = y
            print("Value: %15s -> Steps: %s" % (x, max))


def collatz_plotter(min_value=1, max_value=100, dx=1):
    xas = np.arange(min_value, max_value, dx)
    yas = [collatz(x) for x in range(min_value, max_value)]

    fig, ax = plt.subplots()
    ax.plot(xas, yas)

    ax.set(xlabel='value', ylabel='steps',
           title='Collatz')
    ax.grid()

    fig.savefig("collatz.png")
    plt.show()


if __name__ == '__main__':

    for x in collatz(3):
        print(x)

    # print(collatz(775))
    # print(collatz(763))
    # collatz_plotter(min_value=760, max_value=785)
    # [print("Value: %5s -> Steps: %s" % (x, collatz(x))) for x in range(1, 101)]
    # #
    # col = collatz_generator()
