# code utf-8

def spreadsheet(index):
    i = index
    s = chr(index)
    # while index > 0:
    #     pass
    return(i, s)

if __name__ == '__main__':
    for i in (1, 15, 26, 27, 701, 702, 703, 704, 18277, 18278, 18279, 18280, 675, 30_000, 100_000, 1_000_000):
        print(spreadsheet(i))