# code utf-8
from pprint import pprint

abbreviated = [[227254910, 49.91799, -5.315172, '2013-10-08T22:59:00'],
               [255801560, 49.25383, -4.784833, '2013-10-08T22:59:00'],
               [992271012, 47.64748, -3.509307, '2013-10-08T22:56:00'],
               [227844000, 47.13057, -3.126982, '2013-10-08T22:58:00']]

extended = [[992271012,
             47.64744,
             -3.509282,
             '2013-10-08T21:50:00',
             'PENMEN',
             'FR',
             '',
             ''],
            [227254910,
             49.94479,
             -5.137455,
             '2013-10-08T21:51:00',
             'LAURELINE',
             'FR',
             '',
             'CHERBOURG'],
            [227844000,
             47.23206,
             -2.913887,
             '2013-10-08T21:51:00',
             'NEPTUNE III',
             'FR',
             '',
             ''],
            [255801560,
             49.3815,
             -4.412167,
             '2013-10-08T21:51:00',
             'AUTOPRIDE',
             'PT',
             '',
             'ZEEBRUGGE']]

def index_dict(myList):
    myDict = dict()
    myDict = {l[0]: l for l in myList}
    # pprint(myDict)
    return myDict

def merge(myExtended, myAbbreviated):
    newDict = {boat[0]: [boat[4], boat[5], (boat[1], boat[2], boat[3])] for boat in myExtended}
    # print(f'{newDict}\n')
    for boat in myAbbreviated:
        newDict[boat[0]].append((boat[1], boat[2], boat[3]))
    # pprint(newDict, indent=2)
    return newDict

if __name__ == "__main__":
    d1 = index_dict(abbreviated)
    d2 = index_dict(extended)
    d3 = merge(extended, abbreviated)
    index = 1
    for d in (d1, d2, d3):
        print(f'd{index}:')
        pprint(d)
        index += 1

