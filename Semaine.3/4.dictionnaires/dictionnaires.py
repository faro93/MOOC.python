# code utf-8
import pprint


def graph_dict(filename):
    with open(filename) as f:
        # print(filename)
        lines = f.read().splitlines()
        f.close()

    # print(lines)
    d = dict()
    for line in lines:
        # print(line.split())
        words = line.split()
        # print(words)
        if not words[0] in d:
            d[words[0]] = list()
        d[words[0]].append((words[2], int(words[1])))
    # print(f'd={d}')
    a = {k: d[k] for k in sorted(d)}
    pprint.pprint(a, indent=1)
    return a

if __name__ == '__main__':
    graph_dict('dictionnaires/data/graph1.txt')
    graph_dict('dictionnaires/data/graph2.txt')
    graph_dict('dictionnaires/data/graph3.txt')
