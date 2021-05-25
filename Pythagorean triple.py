def py_triples(u: int, v: int):
    """"This pythagorean triple 'machine' gives any triple corresponded to two integers

    The mathematics behind it uses a complex function f(z) such that f(z) = z**2
    z = u + vi => z**2 = (u**2 - v**2) + (2uv)i
    This means that:
    Re(z) = u**2 - v**2 => this is one side of the right triangle
    Im(z) = 2uv => this is another side of the right triangle
    And the hypotenuse is obviously equal to u**2 + v**2 as that is the product of the squares of the input-values

    We know that u and v are integers so every computations where you only square, add, subtract or multiply
    will result in another integer
    """
    triple = [abs(u ** 2 - v ** 2), 2 * u * v, u ** 2 + v ** 2]
    print(triple)


def ask():
    numbers = input('Input the two numbers separated by a space (u v): ')
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
        py_triples(num_1, num_2)


if __name__ == '__main__':
    loop()
