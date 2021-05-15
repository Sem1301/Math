import sys
from math import *


def wilson(i):
    if i <= 1:
        print("too small")
        return None
    if i > 100000:
        print("too large")
        return None
    n = i - 1
    wil = floor(factorial(n) % (n + 1) / n) * (n - 1) + 2
    if wil == i:
        return wil
    return None


if __name__ == '__main__':
    for i in range(2, 100):
        print(i, wilson(i))
