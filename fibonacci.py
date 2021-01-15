#!/usr/bin/env python3

import sys

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def usage(e):
    print(f"Usage : {sys.argv[0]} <int>")

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

if __name__ == '__main__':
    l = len(sys.argv)
    if l == 2:
        n = sys.argv[1]
        if is_integer(n):
            n = int(n)
            print(fibonacci(n))
        else:
            usage(1)
    else:
        usage(0)
    