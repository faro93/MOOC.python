# coding utf-8

def surgery(liste):
    if len(liste) == 0 or len(liste) == 1:
        return liste
    elif len(liste) % 2 == 0:
        a, b, *c = liste
        return [b, a ,*c]
    else:
        *a, b, c = liste
        return [*a, c, b]

if __name__ == '__main__':
    for s in ([], [0], [1, 0], [0, 2, 1], [1, 0, 2, 3]):
        l = surgery(s)
        print(s, l)