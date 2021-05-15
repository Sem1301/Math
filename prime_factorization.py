import pickle
import time

PRIMES = pickle.load(open("primes_1m.pickle", "rb"))


def prime_factor(n: int) -> list:
    """There is no optimization yet, so large number take a very long time to compute
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


def prime_factors_ivo(n):
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

    sem = []
    ivo = []
    for i in range(5000):
        if i % 50 == 0:
            print("Iteration:", i)

        start = time.time()
        for i in range(201, 5000, 3):
            prime_factors_ivo(i)
        ivo_time = time.time() - start
        ivo.append(ivo_time)

        start = time.time()
        for i in range(201, 5000, 3):
            prime_factor(i)
        sem_time = time.time() - start
        sem.append(sem_time)

    print("Sem:", sum(sem) / len(sem))
    print("Ivo:", sum(ivo) / len(ivo))
