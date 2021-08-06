# code utf-8

def spreadsheet(index):
    s = list()
    mystr = list()
    quotients = list()
    qs = list()
    rs = list()
    alphasize = 26
    A = 64
    if index == 0:
        return None
    else:
        if index > alphasize:
            if (index%alphasize == 0):
                qcur = (index//alphasize)-1
                rcur = 26
                quotients.append((qcur, rcur))
            else:
                quotients.append((index//alphasize, index%alphasize))
                qcur = quotients[0][0]
            while (qcur > alphasize):
                if (qcur%alphasize == 0):
                    qcur = (qcur//alphasize)-1
                    rcur = 26
                    quotients.append((qcur, rcur))
                else:
                    quotients.append((qcur//alphasize, qcur%alphasize))
                qcur = qcur//alphasize
            qs.append(quotients[0][0])
            for (q, r) in quotients[1:]:
                qs.append(q)
                rs.append(r)
            s = qs + rs[::-1]
            s.append(quotients[0][1])
            # print(f'{n} -> {n-1}, quotients={quotients}, s={s} -> ', end="")
            for (i, c) in enumerate(s):
                if c <= alphasize:
                    # print(f'chr({c}+{A})->{chr(c+A)}, ', end="")
                    mystr.append(chr(c+A))
            # print(' ====>>> ', end="")
        else:
            mystr = chr(index+A)
        return ''.join(mystr)

if __name__ == '__main__':
    for i in (1, 15, 26, 27, 701, 702, 703, 704, 18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
    # for i in (18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
        print(f'{i}, {spreadsheet(i)}')
    
    print('################')
    print(f'*** chr(64)="{chr(64)}", chr(65)="{chr(65)}",',
        f'chr(90)="{chr(90)}", chr(91)="{chr(91)}" ***')