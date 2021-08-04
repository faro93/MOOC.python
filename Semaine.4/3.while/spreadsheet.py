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
            q1 = n//alphasize
            qcur = q1
            while (qcur > alphasize):
                s.append(chr(qcur%alphasize+qA))
                qcur = qcur//alphasize
            s.append(chr(qcur+qA))
            s.append(chr(n%alphasize+A))
            n += 1
        else:
            s = chr(n+A)
            n += 1

        return ''.join(s)

# index	q1=index/26     r1=index%26     q2=q1/26    r2=q1%26	CHAR	attendu	formule
# 0     0               0                                       A       A       (r1+65)
# 25  	0   	        25          		        	        Z	    Z       "
# 26    1           	0           		        	        AA	    AA	    (q1+64)&(r1+65)
# 27    1           	1           		        	        AB	    AB      "
# 701 	26          	25          		        	        ZZ	    ZZ	    "
# 702 	27          	0           	1       	1	        AAA	    AAA	    (q2+64)&(r2+64)&(r1+65)
# 727 	27          	25          	1       	1	        AAZ	    AAZ	    "
# 728 	28          	0           	1       	2	        ABA	    ABA	    "
# 753 	28          	25          	1       	2	        ABZ	    ABZ	    "
# 754 	29          	0           	1       	3	        ACA	    ACA	    "
# 755 	29          	1           	1	        3	        ACB	    ACB	    "


if __name__ == '__main__':
    # for i in range(1, 6):
    #     print(f'{i}, {spreadsheet2(i)}')
    # print('################')
    # for i in range(26, 28):
    #     print(f'{i}, {spreadsheet2(i)}')
    # print('################')
    for i in range(702, 704):
        print(f'{i-1}, {spreadsheet2(i)}')
    print('################')
    for i in range(728, 730):
        print(f'{i-1}, {spreadsheet2(i)}')
    print('################')
    for i in range(754, 757):
        print(f'{i-1}, {spreadsheet2(i)}')
    
    # for i in (1, 15, 26, 27, 701, 702, 703, 704, 18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
    #     print(f'{i}, {spreadsheet2(i)}')

    print(f'*** chr(64)={chr(64)}, chr(65)={chr(65)}, chr(90)={chr(90)}, chr(91)={chr(91)} ***')