# coding utf-8
def carre(ligne):
    c = ':'.join([str(int(i)**2) for i in ligne.split(';') if i and i not in (' ', '\t')])
    return c

if __name__ == '__main__':
    for l in ['1;2;3', ' 2 ;  5;6;', '; 12 ;  -23;\t60; 1\t', '; -12 ; ; -23; 1 ;;\t']:
        print(f'{l} -> ', end='')
        print(carre(l))