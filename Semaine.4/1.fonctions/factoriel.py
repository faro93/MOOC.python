# code utf-8

def factoriel(n):
    if isinstance(n, int):
        return 1 if n <= 1 else n * factoriel(n-1)
    elif isinstance(n, str):
        if n.isdigit():
            return factoriel(int(n))
        else:
            raiseFromFactoriel(n)
    elif isinstance(n, (tuple, list)):
        return [factoriel(f) for f in n]
    else:
        raiseFromFactoriel(n)

def raiseFromFactoriel(x):
    raise TypeError(f'{x} {type(x)} is not int.')

if __name__ == '__main__':
    print(factoriel(4))
    print(factoriel("5"))
    print(factoriel((4, "5", 6)))
    # print(factoriel('a'))
    print(factoriel(2.5))