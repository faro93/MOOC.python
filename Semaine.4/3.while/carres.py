# code utf-8

from numbers import Number

# propriétés des log:
# log a(b) = c => b = a**c
# log b(a) + log b(c) = log b(a.c)
# log b(a) - log b(c) = log b(a/c)
# a.log b(c) = log b(c**a)
# log b(a) = log c(a) / log c(b)

# log2(16)= 4 => 16 = 4**2
# log(10_000)= 4 => 10_000 = 10**4
# log(1)= 0 => 1 = 10**0
# log3(27)= 3 => 27 = 3**3
# log(0.1)= -1 => 1 = 10**-1
# log(1/100)= -2 => 1/100 = 10**-2
# log(5)~= 0.699 => 5 = 10**0.699

def power(x, n):
    if n >= 1:
        r = int(1)
        while n > 0:
            r *= x
            # print(f'1.x={x}, n={n}, r={r} ')
            n -= 1
        return r
    else:
        return 1

def power2(x, n):
    if n == 1:
        return x
    elif n%2 == 0:
        r = power2(x, n//2)
        return r * r
    else:
        r = power2(x, n-1)
        return x * r

if __name__ == "__main__":
    for (i, j) in ((2, 1) ,(2, 10), (1j, 4)):
        print(f'{i}**{j} = {power2(i, j)}')