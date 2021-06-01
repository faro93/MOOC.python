# code utf-8

def pgcd(a, b):
    # D = Dividende
    # d = diviseur
    # q = quotient
    D = d = q = int()
    if  a == 0 or b == 0:
        if b ==  0:
            q = a
        elif a == 0:
            q = b
        return q
    elif a >= b:
        (D, d) = (a, b)
        # print(f'(a, b)=({a}, {b}), (D, d)=({D}, {d})')
    elif b >= a:
        (D, d) = (b, a)
        # print(f'(a, b)=({a}, {b}), (D, d)=({D}, {d})')

    while (D%d):
        (D, d) = (d, D%d)
        # print(f'(D, d)=({D}, {d})')
    return d



if __name__ == '__main__':
    for (a, b) in [(0, 0), (0, 1), (1, 0), (15, 10), (10, 15), (3, 10)]:
        print(f'Calcule du PGCD de {a} et {b} : {pgcd(a, b)}')
    (a, b) = (108, 180)
    print(f'Calcule du PGCD de {a} et {b} : {pgcd(a, b)}')
