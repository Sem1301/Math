import os.path
import pickle

PRIME_FILE = os.path.join(os.path.split(__file__)[0], "primes_100m.pickle")


def is_prime(n):
    """
    returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(idx):
    primes = []
    for i in range(2, idx):
        if is_prime(i):
            primes.append(i)
    pickle.dump(primes, open(PRIME_FILE, "wb"))


if __name__ == '__main__':
    generate_primes(100000000)
