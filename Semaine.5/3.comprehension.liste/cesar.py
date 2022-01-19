#code utf-8

import string

def cesar(clear, key, encode=True):
    # print(f'clear="{clear}", key="{key}", encode={encode}')
    if clear not in string.ascii_letters:
        key = 0
        return clear
    else:
        if encode:
            (clear, key_copy, begin) = init_key(clear, key)
            return chr(ord(clear)+(ord(key_copy)-ord(begin))+1)
        else:
            (clear, key_copy, begin) = init_key(clear, key)
            return chr(ord(clear)-(ord(key_copy)-ord(begin))-1)

def init_key(clear, key):
    key_copy = key
    if clear in string.ascii_uppercase:
        begin = string.ascii_uppercase[0]
        if key in string.ascii_lowercase:
            key_copy = key.upper()
    elif clear in string.ascii_lowercase:
        begin = string.ascii_lowercase[0]
        if key in string.ascii_uppercase:
            key_copy = key.lower()
    return (clear, key_copy, begin)

if __name__ == '__main__':
    for i in [('=', 'C'), ('A', 'C'), ('a', 'C'), ('A', 'c'), ('D', 'C', False), ('A', 'L'), ('D', 'C')]:
        print(cesar(*i))
        print()