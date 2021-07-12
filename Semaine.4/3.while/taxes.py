# code utf-8

def taxes(income):
    tranches = [150_000, 50_000, 12_500]
    taux = [0.45, 0.4, 0.2]
    c = 0
    # print(f'0.income = {income}')
    reste = income
    intermediaire = income
    restes = list()

    while c < len(tranches):
        if intermediaire > tranches[c]:
            reste = intermediaire - tranches[c]
            intermediaire = intermediaire - reste
            restes.append((reste, taux[c]))
            # print(f'1.c={c}(>={tranches[c]}) : {reste}, intermediaire = {intermediaire}, taux={taux[c]}')
        c += 1
    # print(restes)

    impot = float()
    for (a, b) in restes:
        impot = impot + a * b
    return(int(impot))

if __name__ == '__main__':
    for montant in (0, 50_000, 12_500, 5_000, 16_500, 30_000, 100_000, 150_000, 200_000, 12_504):
        print(montant, taxes(montant))
