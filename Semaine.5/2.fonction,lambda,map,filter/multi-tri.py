#code utf-8

def multi_tri(listes):
    for i in listes:
        i.sort()
    return listes

if __name__ == '__main__':
    l = [[40, 12, 25], ['spam', 'egg', 'bacon']]
    p = multi_tri(l)
    print(f'p={p}')