# (x * n) mod m = 1


def additiveInverse(n, m):
    x = 1
    while (x * n) % m != 1:
        x += 1
    return x


if __name__ == '__main__':
    n, m = 5, 13
    print(f'Multiplicative Inverse of {n} over modulo {m} is {additiveInverse(n, m)}')
    n, m = 7, 26
    print(f'Multiplicative Inverse of {n} over modulo {m} is {additiveInverse(n, m)}')
