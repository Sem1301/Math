def collatz(a, b):
    """This collatz conjecture script shows the amount of steps needed,
    for a certain interval of numbers to get to 1: (number(n), steps(s))
    """
    for n in range(a, b + 1):
        y = 0
        x = n
        while n != 1:
            y += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
        print('(' + str(x) + ', ' + str(y) + ')')


if __name__ == '__main__':
    collatz(1, 100)
