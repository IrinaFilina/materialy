# Cvičení 3 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci soucet_do(n), která vrátí součet čísel od 1 do n.
#    soucet_do(5) vrátí 15.


def soucet_do(n):
    pocet = 0
    for i in range (1, n+1):
        pocet = pocet + i
    return pocet

print(soucet_do(5))
