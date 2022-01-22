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

if __name__ == '__main__':
    print(cesar('A', 'C'))
    print(cesar('a', 'C'))
    print(cesar('A', 'c'))
    print(cesar('D', 'C', encode=False))
    print(cesar('A', 'L'))
    print(cesar('Z', 'L'))
    print(cesar('a', 'c'))
    print(cesar('N', 'L'))
    print(cesar('O', 'L'))
    print(cesar('D', 'C', encode=False))
    print(cesar('D', 'c', encode=False))
    print(cesar('D', 'c', encode=False))
    print(cesar('a', 'c', True))
    print(cesar('a', 'c', False))
    print(cesar('a', 'J', True))
    print(cesar('a', 'J', False))
    print(cesar('a', 'T', True))
    print(cesar('a', 'T', False))
    print(cesar('a', 'x', True))
    print(cesar('a', 'x', False))
    print(cesar('N', 'c', True))
    print(cesar('N', 'c', False))
    print(cesar('N', 'J', True))
    print(cesar('N', 'J', False))
    print(cesar('N', 'T', True))
    print(cesar('N', 'T', False))
    print(cesar('N', 'x', True))
    print(cesar('N', 'x', False))
    print(cesar('z', 'c', True))
    print(cesar('z', 'c', False))
    print(cesar('z', 'J', True))
    print(cesar('z', 'J', False))
    print(cesar('z', 'T', True))
    print(cesar('z', 'T', False))
    print(cesar('z', 'x', True))
    print(cesar('z', 'x', False))