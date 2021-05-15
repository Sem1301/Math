import pickle
import sys

PRIMES = pickle.load(open("primes_1m.pickle", "rb"))


def prime_factor(n: int) -> list:
    """Prime factors.

    Optimized with pre prepared primes list.
    """
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


if __name__ == '__main__':
    while True:
        to_factor = input('input your integer value here: ')
        if not to_factor:
            sys.exit(0)
        try:
            print(prime_factor(int(to_factor)))
        except IndexError:
            print("Sorry the number you tried is too big.")
