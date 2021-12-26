#code utf-8

def distance(*t):
    if not t:
        return 0
    else:
        r = float()
        for x in t:
            r += x**2
        return r**(1/2)

if __name__ == '__main__':
    r = distance()
    print(r)
    r = distance(1)
    print(r)
    r = distance(1, 1)
    print(r)