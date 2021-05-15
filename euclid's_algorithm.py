
OUTPUT = '''%-20s | %-20s | %-20s'''


def gcd(a, b):
    print(OUTPUT % ('a', 'b', 'a MOD b'))
    print('-' * 80)
    if a > b:
        r = a % b
        started = False
        while r != 0:
            started = True
            r = a % b
            print(OUTPUT % (a, b, r))
            a = b
            b = r
        if started:
            print(a)
        else:
            print(b)
    else:
        print('a must be greater than b')


def ask():
    numbers = input('Input the two numbers separated by a space (a b): ')
    if not numbers:
        return 0, 0

    num_1, num_2 = numbers.split(" ")
    num_1 = int(num_1)
    num_2 = int(num_2)

    return num_1, num_2


def loop():
    running = True
    while running:
        try:
            num_1, num_2 = ask()
        except ValueError:
            print("Syntax error")
            continue
        if num_1 == 0 and num_2 == 0:
            running = False
            continue
        gcd(num_1, num_2)


if __name__ == '__main__':
    loop()
