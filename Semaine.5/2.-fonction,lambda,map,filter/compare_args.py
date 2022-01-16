#code utf-8

from math import factorial
from operator import add

def plus(x, y):
    # print(f'x={x}, y={y}')
    return add(x, y)

def broken_plus(x, y):
    # print(f'x={x}, y={y}')
    if x == 0:
        return add(x, x)
    else:
        return add(x, y)

def fact(x):
    return factorial(x)

def broken_fact(x):
    if x == 0:
        return 0
    else:
        return factorial(x)

def compare_args(f, g, entrees):
    # print(f, g, entrees)
    results = list()
    for x in entrees:
        if f(*x) == g(*x):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    l = [(0,), (1,), (5,)]
    # for i in l:
    #     print(f'f({i})={fact(i)}, g({i})={broken_fact(i)}, type({i})={type(i)}')
    print(compare_args(fact, broken_fact, l))

    l = [(2, 3), (0, 4), (4, 5)]
    # for i in l:
    #     print(f'f({i})={plus(i)}, g({i})={broken_plus(i)}, type({i})={type(i)}')
    print(compare_args(plus, broken_plus, l))
