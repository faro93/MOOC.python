#code utf-8

def scalaire(X, Y):
    s = ((X[i] * Y[i]) for i in range(len(X)))
    r = sum(list(s))
    return r

if __name__ == '__main__':
    print(scalaire((1, 2), (3, 4)))
    print(scalaire((1,2,3,4,5,6), (6,5,4,3,2,1)))