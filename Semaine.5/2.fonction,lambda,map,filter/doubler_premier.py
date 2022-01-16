# code utf-8

from operator import add, mul

def doubler_premier(f, *l):
    if len(l) < 1:
        return None
    else:
        r = l[0]*2
        for i in l[1:]:
            r = f(r, i)
        return r



if __name__ =='__main__':
    for (a, b, c) in [(add, 1, 4), (mul, 1, 4)]:
        r = doubler_premier(a, b, c)
        print(r)
