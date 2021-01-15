#!/usr/bin/python3

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    for i in range(8):
        print(f'fibonacci({i}) : {fibonacci(i)}')