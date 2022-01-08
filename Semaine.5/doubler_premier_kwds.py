# code utf-8

from operator import add, mul

def add3(x, y=0, z=0):
    # print(f'x={x}, y={y}, z={z}')
    return x+y+z

def mul3(x=1, y=1, z=1):
    # print(f'x={x}, y={y}, z={z}')
    return x * y * z

def distance(*l):
    r = float()
    for x in l:
        r = r + x**2
    return r**(1/2)

def doubler_premier_kwds(f, *l, **d):
    # print(f'f={f}, l={l}, d={d}')
    if len(l) < 1:
        return None
    elif len(d) == 0:
        return f(l[0]*2, *l[1:])
    else:
        return f(*(l[0]*2, *l[1:]),**d)

if __name__ =='__main__':
    print(f'résultat={doubler_premier_kwds(add3, 1, 2, 3)}')
    print(f'résultat={doubler_premier_kwds(add3, 1, 2, z=3)}')
    print(f'résultat={doubler_premier_kwds(add3, 1, y=2, z=3)}')
    print(f'résultat={doubler_premier_kwds(mul3, 1, 2, 3)}')
    print(f'résultat={doubler_premier_kwds(mul3, 1, 2, z=3)}')
    print(f'résultat={doubler_premier_kwds(distance, 1.5, 4.0)}')
    print(f'résultat={doubler_premier_kwds(distance, 2.0, 4.0, 4.0, 4.0)}')