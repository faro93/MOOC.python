#code utf-8

import string

def cesar(clear, key, encode=True):
    # print(f'clear="{clear}", key="{key}", encode={encode}', end=' ')
    if clear not in string.ascii_letters:
        key = 0
        return clear
    else:
        if encode:
            (a_orig, a_key) = createListes(clear, key)
            return a_key[a_orig.index(clear)]
 
        else:
            (a_orig, a_key) = createListes(clear, key)
            return a_orig[a_key.index(clear)]

def createListes(clear, key):
    if clear in string.ascii_uppercase:
        key = key.upper()

        # liste ordre alphabétique
        a_orig = [lettre for lettre in string.ascii_uppercase]

        # liste ordre alphabétique décalé de 'key'
        a_key = [a_orig[(i+1+(ord(key)-ord('A')))-len(a_orig)]
                    if i+1+(ord(key)-ord('A')) >= len(a_orig)
                    else a_orig[(i+1+(ord(key)-ord('A')))]
                for (i, lettre) in enumerate(a_orig)]
    else:
        key = key.lower()

        # liste ordre alphabétique
        a_orig = [lettre for lettre in string.ascii_lowercase]

        # liste ordre alphabétique décalé de 'key'
        a_key = [a_orig[(i+1+(ord(key)-ord('a')))-len(a_orig)]
                    if i+1+(ord(key)-ord('a')) >= len(a_orig)
                    else a_orig[(i+1+(ord(key)-ord('a')))]
                for (i, lettre) in enumerate(a_orig)]
    return (a_orig, a_key)

def vigenere(clear, key, encode = True):
    # print(f'msg={clear}, key={key}, encode={encode}')

    r= list()
    for (i,c) in enumerate(clear):
        # print(c, key[i%len(key)], '=', cesar(c, key[i%len(key)], encode))
        r.append(cesar(c, key[i%len(key)], encode))
    return ''.join(r)


if __name__ == '__main__':
    print(vigenere('ce message', 'cle'))
    print('fq pqxvmlh')
    print()
    print(vigenere('fq pqxvmlh', 'CLE', False))
    print('ce message')
    print()
    print(vigenere('une charogne', 'baudelaire'))
    print('woz htbaglpf')
    print()
    print(vigenere('woz htbaglpf', 'baudelaire', False))
    print('une charogne')
    print()
    print(vigenere("Rappelez-vous l'objet", 'Charles'))
    print("Uiqhqqxc-wggx o'ptvjm")
    print()
    print(vigenere("Uiqhqqxc-wggx o'ptvjm", 'Charles', False))
    print("Rappelez-vous l'objet")
    print()
    print(vigenere('que nous vîmes', 'baudelaire'))
    print('svz savb aînzw')
    print()
    print(vigenere('svz savb aînzw', 'baudelaire', False))
    print('que nous vîmes')
