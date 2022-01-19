# code utf-8

def aplatir(*l):
    result = [k for i in l for j in i for k in j]
    return result

if __name__ == '__main__':
    for i in ([], [(1,)], ([1],), [(0, 6, 2), [1, ('a', 4), 5]], ([1, [2, 3]], ('a', 'b', 'c')), ([1, 6], ('c', 'b'), [2, 3]), ((1, [2, 3]), [], 'a', ['b', 'c'])):
        print(aplatir(i))