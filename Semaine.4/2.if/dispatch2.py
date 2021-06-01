# code utf-8

def dispatch2(a, b, A, B):
    if a in A:
        if b in B:
            return a*a + b*b
        else:
            return a*(b-1)
    else:
        if b in B:
            return (a-1)*b
        else:
            return a*a + b*b

if __name__ == '__main__':
    print(dispatch2(3, 7, (2, 4, 6), (8, 10, 6)))