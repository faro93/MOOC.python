# code utf-8

def dispatch1(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return a*a+b*b
        return a*(b-1)
    else:
        if b % 2 == 0:
            return (a-1)*b
        return a*a - b*b

if __name__ == '__main__':
    print(dispatch1(3,7))