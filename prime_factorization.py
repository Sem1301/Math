import pickle
from math import *
import time

from primes_generator import is_prime

PRIMES = pickle.load(open("primes_1m.pickle", "rb"))


def product_factors(factors: list) -> int:
    total = 1
    for factor in factors:
        total *= factor
    # print("product:", total, factor)
    return total


def prime_factor(n: int) -> list:
    """There is no optimization yet, so large number take a very long time to compute
    """
    # if is_prime(n):
    #     return [n, ]
    idx = 0
    i = PRIMES[idx]
    factors = []
    while i <= n:
        while n % i == 0:
            n /= i
            factors.append(i)
        idx += 1
        i = PRIMES[idx]
        if n < i * i:
            if n > 1:
                factors.append(int(n))
            break
    return factors


def prime_factor_Sem(n: int) -> list:
    """There is no optimization yet, so large number take a very long time to compute
    """
    orig = n
    if is_prime(n):
        return [n, ]
    idx = 0
    i = PRIMES[idx]
    factors = []
    while i <= n:
        if n < 2 * i:
            factors.append(int(n))
            if product_factors(factors) == orig:
                return factors
            i = n
        elif n % i == 0:
            n /= i
            factors.append(i)
        else:
            idx += 1
            i = PRIMES[idx]
    return factors


def prime_factors_2(n):
    """Returns all the prime factors of a positive integer
    used in "opgave 22" of 2017
    """
    factors = []
    idx = 0
    d = PRIMES[idx]
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(int(n))
            break
    return factors


def prime_factors_3(n):
    """Returns all the prime factors of a positive integer
    used in "opgave 22" of 2017
    """
    factors = []
    idx = 0
    d = PRIMES[idx]
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        idx += 1
        d = PRIMES[idx]
        if d * d > n:
            if n > 1:
                factors.append(int(n))
            break
    return factors


if __name__ == '__main__':
    # print(prime_factor(int(input('input your integer value here: '))))

    print("=" * 80)
    print("Sem")
    print("=" * 80)
    start = time.time()
    for i in range(201, 5000, 3):
        # print(i, prime_factor(i))
        prime_factor(i)
    print("Sem:", time.time() - start)
    print("=" * 80)
    print("Ivo")
    print("=" * 80)
    start = time.time()
    for i in range(201, 5000, 3):
        # print(prime_factors_2(i))
        prime_factors_2(i)
    print("Ivo2:", time.time() - start)
    start = time.time()
    for i in range(201, 5000, 3):
        # print(i, prime_factors_2(i))
        prime_factors_3(i)
    print("Ivo3:", time.time() - start)
