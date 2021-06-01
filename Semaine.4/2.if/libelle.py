# code utf-8

def libelle(ligne):
    champs = ligne.split(',')
    for (i, s) in enumerate(champs):
        champs[i] = s.strip()

    if len(champs) == 3:
        srang = '-ème'
        if champs[2] != '':
            irang = int(champs[2])
            if irang == 1:
                srang = '1er'
            elif irang == 2:
                srang = '2nd'
            else:
                srang = str(irang) + srang

        if not '' in champs:
            return f'{champs[1]}.{champs[0]} ({srang})'
        else:
            if champs[2] == '':
                return f'{champs[1]}.{champs[0]} ({srang})'
    else:
        return None

if __name__ == '__main__':
    for s in ('Joseph, Dupont, 4'), ('Jean'), ('Jules , Durand, 1'), (' Ted, Mosby, 2,'),\
                (' Jacques , Martin, 3 \t'), ('Sheldon, Cooper ,5,  '), ('\t John, Doe\t, '),\
                ('John, Smith, , , , 3'):
        print(libelle(s))