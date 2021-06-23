# code utf-8

def taxes(income):
    print(income)
    reste = income
    impot = int()
    while reste > 0:
        if reste < 12_500:
            return impot
        elif 12_501 <= reste <= 50_000:
            reste -= 

if __name__ == '__main__':
    for taxe in (0, 7500, 12500):
        taxes(taxe)