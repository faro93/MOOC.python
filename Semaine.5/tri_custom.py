# code utf-8

import copy

def tri_custom(liste):
    d = dict()
    n = list()
    p = list()
    p2 = list()
    r = list()
    for d1 in liste:
        n.append(d1['n'])
        p.append(d1['p'])
        if not 'p2' in d1.keys():
            p2.append('')
        else:
            p2.append(d1['p2'])

    all = sorted(list(zip(n, p, p2)))
    for i in all:
        d['n'] = i[0]
        d['p'] = i[1]
        if i[2] != '':
            d['p2'] = i[2]
        r.append(copy.deepcopy(d))
    return r


if __name__ == '__main__':
    r = tri_custom([
        { 'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
        { 'n': 'Martin', 'p': 'Jean'},
        { 'n': 'Martin', 'p': 'Jeanneot'},
        { 'n': 'Dupont', 'p': 'Alex'},
        { 'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
        { 'n': 'Martin', 'p': 'Jeanne'},
        { 'n': 'Dupont', 'p': 'Alexandre'},
        { 'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
        { 'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
        { 'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
        { 'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
        { 'n': 'Dupont', 'p': 'Laura'}
        ])
    print(r)

# attendu
    #[{ 'n': 'Dupont','p': 'Alex'},
    # { 'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
    # { 'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
    # { 'n': 'Dupont', 'p': 'Alexandre'},
    # { 'n': 'Martin', 'p': 'Jean'},
    # { 'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
    # { 'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
    # { 'n': 'Martin', 'p': 'Jeanne'},
    # { 'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
    # { 'n': 'Martin', 'p': 'Jeanneot'},
    # { 'n': 'Dupont', 'p': 'Laura'},
    # { 'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'}]