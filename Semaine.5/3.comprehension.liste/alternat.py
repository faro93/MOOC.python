# code utf-8

def alternat(c1, c2):
    # result = list()
    # l = list(zip(c1, c2))
    # print(f'l={l}')
    # for i in l:
    #     print(f'i={i}')
    #     for j in i:
    #         print(f'j={j}')
    #         result.append(j)
    # print(f'result={result}')
    l = list(zip(c1, c2))
    return [j for i in l for j in i]

if __name__ == '__main__':
    for c1, c2 in (((1, 2), ('a', 'b')), ((1, 2, 3), ('a', 'b', 'c'))):
        print(alternat(c1, c2))