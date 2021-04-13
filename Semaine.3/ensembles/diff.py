# code utf-8
from pprint import pprint

Extended = [
    [309253000, 49.41672, -3.996833, '2013-10-08T21:51:00', 'GRACEFUL LEADER', 'BS', '', 'CASABLANCA'],
    [215517000, 49.3434, -4.178375, '2013-10-08T21:51:00', 'ALYCIA', 'MT', '', 'NUEVA PALMIRA'],
    [245718000, 49.8989, -5.240509, '2013-10-08T21:51:00', 'AMAZONE', 'NL', '', 'DUNKERQUE'],
    [224175430, 47.20671, -5.877663, '2013-10-08T21:50:00', 'ADVIENTO UNO', 'ES', '', '']
    ]

Abbreviated = [
    [224175430, 47.21678, -5.869355, '2013-10-08T22:59:00'],
    [245718000, 49.92569, -5.524793, '2013-10-08T22:59:00'],
    [227115520, 48.09115, -4.333058, '2013-10-08T22:55:00'],
    [228240900, 47.19841, -2.723277, '2013-10-08T22:55:00']
    ]

def diff(extended, abbreviated):
    # print(f'type de extended : {type(extended)}')
    # pprint(extended)
    # print(f'type de extended : {type(abbreviated)}')
    # pprint(abbreviated)
    dext = index_dict(extended)
    dabb = index_dict(abbreviated)
    pprint(dext)
    pprint(dabb)

    

def index_dict(myList):
    myDict = dict()
    myDict = {l[0]: l for l in myList}
    return myDict

if __name__ == '__main__':
    l = diff(Extended, Abbreviated)
    # pprint(l)