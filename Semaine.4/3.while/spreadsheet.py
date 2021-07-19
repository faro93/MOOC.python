# code utf-8

def spreadsheet(n):
    s = str()
    if n > 26:
        q = n/27
        r = n % 27
        s += chr(int(q)+64)+chr(r+65)
    else:
        s = chr(n+64)

    print(n, s)

if __name__ == '__main__':
    for i in range(1, 58):
        spreadsheet(i)
    print(chr(64), chr(65), chr(65+27))
    # for i in (1, 15, 26, 27, 701, 702, 703, 704, 18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
    #     print(spreadsheet(i))