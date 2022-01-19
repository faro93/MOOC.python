# code utf-8

def intersect(a, b):
    # print(f'a={a}, b={b}')
    # result = list()
    # A = dict(a)
    # B = dict(b)
    # print(f'A={A}, B={B}')
    # for k in A.keys():
    #     if k in B.keys():
    #         result.append(B[k])
    #         result.append(A[k])
    # print(f'result={set(result)}')

    # for i in l:
    #     print(f'i={i}')
    #     for j in i:
    #         print(f'j={j}')
    #         result.append(j)
    # print(f'result={set(result)}')

    result = list()
    A = dict(a)
    B = dict(b)
    l = {(B[k],A[k]) for k in A.keys() if k in B.keys()}
    result = {j for i in l for j in i}
    # print(f'result={result}')
    return result




if __name__ == '__main__':
    for A, B in (  ({(8, 'huit'), (10, 'dixA'), (12, 'douze')},
                    {(5, 'cinq'), (10, 'dixB'), (15, 'quinze')}),
                ({(1, 'unA'), (2, 'deux'), (3, 'troisA')},
                    {(1, 'unB'), (2, 'deux'), (4, 'quatreB')})):
        print(intersect(A, B))