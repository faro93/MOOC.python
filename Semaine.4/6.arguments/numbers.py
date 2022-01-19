#code utf-8

def numbers(*t):
    if not t:
        return (0, 0, 0)
    else:
        s = somme(t)
        return (s, min(t), max(t))

def somme(t):
    s = int()
    for x in t:
        s += x
    return s

if __name__ == '__main__':
    r = numbers()
    print(r)
    r = numbers(6)
    print(r)
    r = numbers(11, 11, 6, 6, 7)
    print(r)