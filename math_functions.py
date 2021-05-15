def gcd(a: int, b: int) -> int:
    """"Greatest Common Denominator.
    """
    if a > b:
        r = a % b
        started = False
        while r != 0:
            started = True
            r = a % b
            a = b
            b = r
        if started:
            return a
        else:
            return b
    else:
        raise ValueError('a must be greater than b')


def product_list(numbers: list) -> int:
    total = 1
    for num in numbers:
        total *= num
    return total


def prime_factor(n: int) -> list:
    """Prime factors.
    """
    i = 2
    factors = []
    while i <= n:
        while n % i == 0:
            n /= i
            factors.append(i)
        i += 1
        if n < i * i:
            if n > 1:
                factors.append(int(n))
            break
    return factors


if __name__ == '__main__':
    print(prime_factor(int(input('input your integer value here: '))))
