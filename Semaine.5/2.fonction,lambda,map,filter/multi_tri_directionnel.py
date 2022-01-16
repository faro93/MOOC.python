#code utf-8

def multi_tri(listes, reverses):
    for i, l in enumerate(listes):
        l.sort(reverse=reverses[i])
    return listes

if __name__ == '__main__':
    l1 = [[1, 2], [3, 4]]
    l2 = [True, False]
    p = multi_tri(l1, l2)
    print(f'p={p}')