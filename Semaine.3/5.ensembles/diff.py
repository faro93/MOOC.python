# code utf-8
from pprint import pprint
import json

Extended = [
    [636011581, 48.82042, -2.584033, '2013-10-08T21:51:00', 'ATLANTIC SURVEYOR', 'LR', '', 'LE HAVRE'],
    [227820000, 47.47211, -4.327153, '2013-10-08T21:51:00', 'NOTRE DAME', 'FR', '', 'ROSCOFF'],
    [228893000, 47.79529, -4.278713, '2013-10-08T21:50:00', 'LE COMMODORE', 'FR', '', ''],
    [228219600, 47.07186, -2.808102, '2013-10-08T21:51:00', 'ANDRE L', 'FR', '', 'LES SABLES D OLONNE']
    ]

Abbreviated = [
    [228893000, 47.79529, -4.278713, '2013-10-08T22:51:00'],
    [228219600, 47.20869, -2.936868, '2013-10-08T22:59:00'],
    [227115520, 48.09115, -4.333058, '2013-10-08T22:55:00'],
    [228240900, 47.19841, -2.723277, '2013-10-08T22:55:00']
    ]

def diff(extended, abbreviated):
    dext = index_dict(extended)
    dabb = index_dict(abbreviated)

    inExtOnly = BoatsInEntendedOnly(dext, dabb)
    inBoth = BoatsInExtendedAndAbbreviated(dext, dabb)
    inAbbOnly = BoatsInAbbreviatedOnly(dext, dabb)
    return (inExtOnly, inBoth, inAbbOnly)

def BoatsInEntendedOnly(extended, abbreviated):
    boats = {extended[k][4] for k in extended if k not in abbreviated.keys()}
    return boats

def BoatsInExtendedAndAbbreviated(extended, abbreviated):
    boats = {extended[k][4] for k in extended if k in abbreviated.keys()}
    return boats

def BoatsInAbbreviatedOnly(extended, abbreviated):
    boats = {k for k in abbreviated if k not in extended.keys()}
    return boats

def index_dict(myList):
    myDict = dict()
    myDict = {l[0]: l for l in myList}
    return myDict

def loadJSON(filename):
    with open(filename, encoding="utf-8") as feed:
        fulldata = json.load(feed)
        return fulldata

if __name__ == '__main__':
    l = diff(Extended, Abbreviated)
    pprint(l)
    extended_full = loadJSON('Semaine.3/ensembles/data/marine-e2-ext.json')
    abbreviated_full = loadJSON('Semaine.3/ensembles/data/marine-e2-abb.json')
    l = diff(extended_full, abbreviated_full)
    pprint(l)