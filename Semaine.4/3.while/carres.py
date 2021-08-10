# code utf-8
# log a(b) = c => b = a**c
# log2(16)= 4 => 16 = 4**2
# log(10_000)= 4 => 10_000 = 10**4
# log(1)= 0 => 1 = 10**0
# log3(27)= 3 => 27 = 3**3
# log(0.1)= -1 => 1 = 10**-1
# log(1/100)= -2 => 1/100 = 10**-2
# log(5)~= 0.699 => 5 = 10**0.699

def power(x, n):
    # print(f'x={x}, n={n} ')
    if n >= 1:
        return f'{x}, {n}'
    else:
        return f'Erreur : {n} < 1'

if __name__ == "__main__":
    for (i, j) in ((4, 2), (3, 3), (10, 0)):
        print(f'{i}**{j} = {power(i, j)}')