# code utf-8
'''
Dans un notebook:
a = [ i for i in range(5000000)]
print(len(a))
%timeit -n 1000 33333 in a
5000000
419 µs ± 21.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

s = set(a)
print(len(s))
%timeit -n 1000 33333 in s
5000000
49.6 ns ± 2.68 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
'''

import timeit
import_module = "import random"

repeat = 10_000

list_code = '''a = [i for i in range(50000)]
s = set(a)
random.randint(0, 49999) in a'''

set_code = '''a = [i for i in range(50000)]
s = set(a)
random.randint(0, 49999) in s'''

for code in (list_code, set_code):
    print(f'Exécution {repeat} fois du code suivant :\n{code}')
    print(f'Durée d\'exécution : {timeit.timeit(stmt=code, setup=import_module, number=repeat)}s')
    print()
