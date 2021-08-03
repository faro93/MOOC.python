# code utf-8

def spreadsheet(n):
    s = str()
    alphasize = 26
    A = 65
    if n == 0:
        return None
    else:
        n -= 1
        if n > alphasize-1:
            q = n//(alphasize)
            r = n % (alphasize)
            qc = 64
            q1 = q+qc
            r1 = r+A
            s += chr(q1) + chr(r1)
            n += 1
            print(f'n={n}, q={q}, r={r}, s={s}(chr({q}+{qc}={q1}) + chr({r}+{A}={r1})) --> ', end = '')
        else:
            s = chr(n+A)
            n += 1

        return s

def spreadsheet2(n):
    s = list()
    alphasize = 26
    A = 65
    qA = 64
    if n == 0:
        return None
    else:
        n -= 1
        if n > alphasize-1:
            q = n//alphasize
            qcur = q
            while (qcur > alphasize):
                s.append(chr(qcur%alphasize+qA))
                qcur = qcur//alphasize
            r = n % alphasize
            r1 = r+A
            s.append(chr(qcur+qA))
            s.append(chr(r1))
            n += 1
            # print(f'n={n}, q={q}, r={r}, s={s}(chr({q}+{qc}={q1}) + chr({r}+{A}={r1})) --> ', end = '')
        else:
            s = chr(n+A)
            n += 1

        return ''.join(s)

if __name__ == '__main__':
    # for i in range(0, 84):
    #     print(spreadsheet(i))
    for i in range(600, 801):
        print(f'{i}, {spreadsheet2(i)}')
    
    # for i in (1, 15, 26, 27, 701, 702, 703, 704, 18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
    #     print(spreadsheet(i))

    print(f'*** chr(64)={chr(64)}, chr(65)={chr(65)}, chr(90)={chr(90)}, chr(91)={chr(91)} ***')