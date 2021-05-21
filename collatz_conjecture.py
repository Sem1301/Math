import os

import matplotlib.pyplot as plt
import numpy as np

COLLATZ_PATH = os.path.join(os.path.split(__file__)[0], "collatz_plots")
try:
    os.mkdir(COLLATZ_PATH)
except IOError:
    pass


# from math_functions import collatz

def collatz(value):
    """TODO doc
    This collatz conjecture script shows the amount of steps needed,
    for a certain interval of integers to get to 1: (integer(i), steps(s))
    It only works for positive integers {1, 2, 3, ...}
    """
    i = value
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        yield int(i)


def collatz_generator(start=1):
    num = start
    while True:
        yield num, collatz(num)
        num += 1


def collatz_plotter():
    for item in range(2, 100):
        yas = []
        for idx, y in enumerate(collatz(item), start=1):
            yas.append(y)
        xas = np.arange(1, len(yas) + 1, 1)

        fig, ax = plt.subplots()
        ax.plot(xas, yas)

        ax.set(xlabel='value', ylabel='steps',
               title='Collatz')
        ax.grid()

        fig.savefig(os.path.join(COLLATZ_PATH, "collatz%s.png" % item))
        plt.close(fig)
        # plt.show()


def max_steps():
    max = 0
    for x, y in collatz_generator(15733191):
        if y > max:
            max = y
            print("Value: %15s -> Steps: %s" % (x, max))


if __name__ == '__main__':
    collatz_plotter()
    # for idx, x in enumerate(collatz(3), start=1):
    #     print(idx, x)

    # print(collatz(775))
    # print(collatz(763))
    # collatz_plotter(min_value=760, max_value=785)
    # [print("Value: %5s -> Steps: %s" % (x, collatz(x))) for x in range(1, 101)]
    # #
    # col = collatz_generator()
