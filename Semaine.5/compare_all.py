#code utf-8

from math import factorial

def fact(x):
    return factorial(x)

def broken_fact(x):
    if x == 0:
        return 0
    else:
        return factorial(x)

def compare_all(f, g, entrees):
    # print(f, g, entrees)
    results = list()
    for x in entrees:
        if f(x) == g(x):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    l = [0, 1, 5]
    for i in l:
        print(f'f({i})={fact(i)}, g({i})={broken_fact(i)}')
    print(compare_all(fact, broken_fact, l))