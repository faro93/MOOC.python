# code utf-8
import pprint

def read_set(filename):
    # print(filename)
    with open(filename) as f:
        lines = f.read().splitlines()
        f.close()
    lines = {i.strip() for i in sorted(lines)}
    return lines

def search_in_set(filename_reference, filename):
    table = list()
    # print(filename_reference, filename)
    ref = read_set(filename_reference)
    # print(type(ref), ref)
    with open(filename) as f:
        lines = f.read().splitlines()
        f.close()
    for line in lines:
        if line.strip() in ref:
            table.append((line.strip(), True))
        else:
            table.append((line.strip(), False))
    # print(table)
    return table

if __name__ == '__main__':
    # s = read_set('ensembles/data/setref1.txt')
    # print(s)
    t = search_in_set('ensembles/data/setref1.txt', 'ensembles/data/setsample1.txt')
    pprint.pprint(t)