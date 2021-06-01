#coding utf-8

def wc(string):
    # remplacer pass par votre code
    liste = list()
    liste.append(string.count('\n'))
    liste.append(len(string.split()))
    liste.append(len(string))
    return liste


if __name__ == '__main__':
    for s in (('Python is a programming language\n'
            'that lets you work quickly\n'
            'and integrate systems more effectively.'),#[2, 15, 99]
            '',#[0, 0, 0]
            'abc',#[0, 1, 3]
            'abc \t',#[0, 1, 5]
            'a  bc \t',#[0, 2, 7]
            ' \tabc \n',#[1, 1, 7]
            'a b c d e f g\n',#[1, 7, 14]
            (   'The Zen of Python, by Tim Peters\n'
                '\n'
                'Beautiful is better than ugly.\n'
                'Explicit is better than implicit.\n'
                'Simple is better than complex.\n'
                'Complex is better than complicated.\n'
                'Flat is better than nested.\n'
                'Sparse is better than dense.\n'
                '...')#[8, 38, 226]
            ):
        r = wc(s)
        print(r)